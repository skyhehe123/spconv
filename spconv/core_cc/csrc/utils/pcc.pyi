from typing import overload, Any, Callable, Dict, List, Optional, Set, Tuple, Type, Union
from pccm.stubs import EnumValue, EnumClassValue, enum
from cumm.tensorview import Tensor
class PointCloudCompress:
    @staticmethod
    def encode_with_order(points: Tensor, intensity: Tensor, ex: float, ey: float, ez: float, type, with_order: bool = False) -> Tuple[Tensor, Tensor]: 
        """
        Args:
            points: 
            intensity: 
            ex: 
            ey: 
            ez: 
            type: 
            with_order: 
        """
        ...
    @staticmethod
    def encode_xyzi(points: Tensor, intensity: Tensor, ex: float, ey: float, ez: float) -> Tensor: 
        """
        Args:
            points: 
            intensity: 
            ex: 
            ey: 
            ez: 
        """
        ...
    @staticmethod
    def encode_xyz(points: Tensor, ex: float, ey: float, ez: float) -> Tensor: 
        """
        Args:
            points: 
            ex: 
            ey: 
            ez: 
        """
        ...
    @staticmethod
    def decode(data: Tensor) -> Tensor: 
        """
        Args:
            data: 
        """
        ...
    class EncodeType(enum.Enum):
        XYZ_8 = 0
        XYZI_8 = 1
        @staticmethod
        def __members__() -> Dict[str, EnumClassValue]: ...
