from __future__ import annotations

from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class OdbDataMaterial:
    """The OdbDataMaterial object stores material data.

    .. note::
        This object can be accessed by::

            import visualization
            session.odbData[name].materials[i]
    """

    #: A String specifying the set name. This attribute is read-only.
    name: str = ""

    #: A String-to-tuple-of-Ints Dictionary specifying the elements in the set. This attribute
    #: is read-only.
    elements: str = ""
