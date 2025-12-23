# Copyright (c) OpenMMLab. All rights reserved.
"""COCO API compatibility layer.

Prefer xtcocotools when available, fall back to pycocotools.
"""

try:
    from xtcocotools.coco import COCO  # type: ignore
    from xtcocotools.cocoeval import COCOeval  # type: ignore
    import xtcocotools.mask as mask  # type: ignore

    COCOAPI = 'xtcocotools'
except Exception:
    try:
        from pycocotools.coco import COCO  # type: ignore
        from pycocotools.cocoeval import COCOeval  # type: ignore
        import pycocotools.mask as mask  # type: ignore

        COCOAPI = 'pycocotools'
    except Exception as exc:
        raise ImportError(
            'COCO API is required but neither xtcocotools nor pycocotools '
            'is available. Install xtcocotools (recommended) or pycocotools.'
        ) from exc

__all__ = ['COCO', 'COCOeval', 'mask', 'COCOAPI']
