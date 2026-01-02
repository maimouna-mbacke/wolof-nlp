"""Wolof Spatial Semantics - Body-based orientation and locatives"""

from dataclasses import dataclass
from typing import Optional
from enum import Enum, auto

class SpatialRegion(Enum):
    FRONT = auto()
    BACK = auto()
    INSIDE = auto()
    OUTSIDE = auto()
    ABOVE = auto()
    BELOW = auto()
    SIDE = auto()
    NEAR = auto()

@dataclass
class SpatialExpression:
    word: str
    region: SpatialRegion
    body_part_origin: Optional[str]
    preposition: bool
    temporal_extension: Optional[str]

SPATIAL_TERMS = {
    'kanam': SpatialExpression('kanam', SpatialRegion.FRONT, 'face', False, 'future'),
    'gannaaw': SpatialExpression('gannaaw', SpatialRegion.BACK, 'back', False, 'past'),
    'biir': SpatialExpression('biir', SpatialRegion.INSIDE, 'belly', False, None),
    'biti': SpatialExpression('biti', SpatialRegion.OUTSIDE, None, False, None),
    'kow': SpatialExpression('kow', SpatialRegion.ABOVE, None, False, None),
    'suuf': SpatialExpression('suuf', SpatialRegion.BELOW, 'ground', False, None),
    'wetu': SpatialExpression('wetu', SpatialRegion.SIDE, None, True, None),
    'ci': SpatialExpression('ci', SpatialRegion.NEAR, None, True, None),
    'ca': SpatialExpression('ca', SpatialRegion.NEAR, None, True, None),
    'fi': SpatialExpression('fi', SpatialRegion.NEAR, None, True, None),
    'fa': SpatialExpression('fa', SpatialRegion.NEAR, None, True, None),
}

class SpatialAnalyzer:
    def analyze(self, word: str) -> Optional[SpatialExpression]:
        return SPATIAL_TERMS.get(word.lower())
    
    def get_locatives(self) -> dict:
        return {
            'proximal': ['ci', 'fi', 'fii'],
            'medial': ['ca', 'fa', 'fee'],
            'distal': ['ca', 'fa', 'foofu'],
        }
    
    def has_temporal_extension(self, word: str) -> bool:
        expr = self.analyze(word)
        return expr is not None and expr.temporal_extension is not None

def analyze_spatial(word: str) -> Optional[SpatialExpression]:
    return SpatialAnalyzer().analyze(word)