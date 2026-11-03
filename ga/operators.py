import random
import copy
from typing import List, Dict, Any, Tuple
from ga.individual import Chromosome, Gene
import mr_library

ALL_MR_IDS = mr_library.list_mrs()


def validate_gene_params(gene: Gene) -> bool:
    """Strict invariant validator. Returns False if parameters violate physical or logical constraints."""
    params = gene.params
    if gene.mr_id == "ChangeCouplingMap":
        min_dens = params.get("min_connection_density")
        max_dens = params.get("max_connection_density")
        if min_dens is not None and max_dens is not None:
            if min_dens > max_dens:
                return False
        min_nodes = params.get("min_perc_nodes")
        max_nodes = params.get("max_perc_nodes")
        if min_nodes is not None and max_nodes is not None:
            if min_nodes > max_nodes:
                return False
    elif gene.mr_id == "AddUnusedRegister":
        min_b = params.get("min_n_bit", 1)
        max_b = params.get("max_n_bit", 10)
        if min_b > max_b:
            return False
    return True


def sample_random_gene(mr_id: str = None) -> Gene:
    """Create a gene with a randomly selected MR and strictly valid sampled parameters."""
    if mr_id is None:
        mr_id = random.choice(ALL_MR_IDS)
    
    info = mr_library.get_mr_info(mr_id) or {}
    params_meta = info.get("parameters", {})
    params = {}
    
    for p_name, p_info in params_meta.items():
        params[p_name] = copy.deepcopy(p_info.get("default"))

    # Parameter sampling with enforced constraints
    if mr_id == "ChangeOptLevel":
        params["levels"] = random.sample([0, 1, 2, 3], random.randint(1, 4))
    elif mr_id == "ChangeCouplingMap":
        min_dens = round(random.uniform(0.05, 0.15), 2)
        max_dens = round(random.uniform(min_dens + 0.05, 0.30), 2)
        params["min_connection_density"] = min_dens
        params["max_connection_density"] = max_dens
        params["min_perc_nodes"] = 1
        params["max_perc_nodes"] = round(random.uniform(1.1, 1.8), 2)
        params["force_connected"] = True
    elif mr_id == "ChangeTargetBasis":
        val = params_meta.get("universal_gate_sets", {}).get("default", [])
        if val:
            params["universal_gate_sets"] = [random.choice(val)]
    elif mr_id == "ChangeQubitOrder":
        params["scramble_percentage"] = random.choice([0.5, 0.75, 1.0])
    elif mr_id == "InjectParameters":
        params["p_fraction"] = round(random.uniform(0.1, 0.5), 2)
    elif mr_id == "ChangeBackend":
        val = params_meta.get("available_backends", {}).get("default", [])
        if val:
            params["available_backends"] = random.sample(val, max(1, random.randint(1, len(val))))
            
    gene = Gene(mr_id=mr_id, params=params)
    assert validate_gene_params(gene), f"Generated invalid gene parameters for {mr_id}: {params}"
    return gene


def initialize_population(pop_size: int = 80, depth_min: int = 2, depth_max: int = 3) -> List[Chromosome]:
    """Generate initial population of chromosomes."""
    population = []
    for _ in range(pop_size):
        depth = random.randint(depth_min, depth_max)
        genes = [sample_random_gene() for _ in range(depth)]
        population.append(Chromosome(genes=genes))
    return population


def tournament_selection(population: List[Chromosome], tourn_size: int = 4) -> Chromosome:
    """Tournament selection with user-confirmed tourn_size = 4."""
    candidates = random.sample(population, min(tourn_size, len(population)))
    return max(candidates, key=lambda ind: ind.fitness)


def crossover(parent1: Chromosome, parent2: Chromosome, depth_min: int = 2, depth_max: int = 3) -> Tuple[Chromosome, Chromosome]:
    """Single-point crossover between two parent chromosomes."""
    if len(parent1.genes) < 2 or len(parent2.genes) < 2:
        return copy.deepcopy(parent1), copy.deepcopy(parent2)

    pt1 = random.randint(1, len(parent1.genes) - 1)
    pt2 = random.randint(1, len(parent2.genes) - 1)

    c1_genes = copy.deepcopy(parent1.genes[:pt1] + parent2.genes[pt2:])
    c2_genes = copy.deepcopy(parent2.genes[:pt2] + parent1.genes[pt1:])

    # Clamp depths within [depth_min, depth_max]
    def clamp(genes):
        if len(genes) > depth_max:
            return genes[:depth_max]
        while len(genes) < depth_min:
            genes.append(sample_random_gene())
        return genes

    child1 = Chromosome(genes=clamp(c1_genes))
    child2 = Chromosome(genes=clamp(c2_genes))
    return child1, child2


def mutate(chromosome: Chromosome, p_mut_gene: float = 0.25) -> Chromosome:
    """Mutates genes: 60% parameter tweak, 30% replace MR, 10% swap adjacent."""
    mutated_genes = copy.deepcopy(chromosome.genes)

    for i in range(len(mutated_genes)):
        if random.random() < p_mut_gene:
            r = random.random()
            if r < 0.60:
                # Parameter tweak
                gene = mutated_genes[i]
                mutated_genes[i] = sample_random_gene(gene.mr_id)
            elif r < 0.90:
                # Replace whole MR
                new_mr = random.choice(ALL_MR_IDS)
                mutated_genes[i] = sample_random_gene(new_mr)
            else:
                # Swap with neighbor
                if len(mutated_genes) > 1:
                    j = (i + 1) % len(mutated_genes)
                    mutated_genes[i], mutated_genes[j] = mutated_genes[j], mutated_genes[i]

    return Chromosome(genes=mutated_genes)


def select_elites(population: List[Chromosome], elite_cnt: int = 4) -> List[Chromosome]:
    """Extract top elite chromosomes."""
    sorted_pop = sorted(population, key=lambda c: c.fitness, reverse=True)
    return [copy.deepcopy(ind) for ind in sorted_pop[:elite_cnt]]
