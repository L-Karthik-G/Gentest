import json
import uuid
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional


@dataclass
class Gene:
    mr_id: str
    params: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "mr_id": self.mr_id,
            "params": self.params
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Gene":
        return cls(mr_id=data["mr_id"], params=data.get("params", {}))


@dataclass
class Chromosome:
    id: str = field(default_factory=lambda: f"mr_comp_{uuid.uuid4().hex[:8]}")
    genes: List[Gene] = field(default_factory=list)
    fitness: float = -float("inf")
    objectives: Dict[str, float] = field(default_factory=dict)
    is_valid: bool = False
    error_msg: str = ""
    generated_code: Optional[str] = None
    qasm3: Optional[str] = None
    generation: int = 0

    @property
    def depth(self) -> int:
        return len(self.genes)

    def signature(self) -> str:
        """Structural signature of the MR composition chain."""
        return " -> ".join([f"{g.mr_id}({list(g.params.keys())})" for g in self.genes])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "signature": self.signature(),
            "depth": self.depth,
            "fitness": self.fitness,
            "objectives": self.objectives,
            "is_valid": self.is_valid,
            "generation": self.generation,
            "genes": [g.to_dict() for g in self.genes],
            "error_msg": self.error_msg
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Chromosome":
        genes = [Gene.from_dict(g) for g in data.get("genes", [])]
        chrom = cls(
            id=data.get("id", f"mr_comp_{uuid.uuid4().hex[:8]}"),
            genes=genes,
            fitness=data.get("fitness", -float("inf")),
            objectives=data.get("objectives", {}),
            is_valid=data.get("is_valid", False),
            error_msg=data.get("error_msg", ""),
            generation=data.get("generation", 0)
        )
        return chrom
