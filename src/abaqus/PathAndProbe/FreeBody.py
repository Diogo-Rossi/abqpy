from __future__ import annotations

from typing_extensions import Dict, Literal, Tuple

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import CENTROID, NORMAL_TANGENTIAL, OFF, Boolean
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class FreeBody:
    """The FreeBody object defines a section across which resultant forces and moments are computed.

    .. note::
        This object can be accessed by::

            import visualization
            session.freeBodies[name]
    """

    @abaqus_method_doc
    def FreeBodyFromEdges(
        self,
        name: str,
        edges: str,
        summationLoc: Literal[C.SPECIFY, C.CENTROID, C.NODAL_AVERAGE] = CENTROID,
        summationPoint: tuple = (),
        componentResolution: Literal[C.NORMAL_TANGENTIAL, C.CSYS] = NORMAL_TANGENTIAL,
        csysName: str = "",
    ):
        """This method creates a FreeBody object and places it in the freeBodies repository.

        .. note::
            This function can be accessed by::

                session.FreeBodyFromEdges

        Parameters
        ----------
        name
            A string name for the free body.
        edges
            A DisplayGroup leaf object that specifies the physical constituents of the free body.
        summationLoc
            A SymbolicConstant specifying the location of the summation point. Possible values are
            CENTROID, NODAL_AVERAGE and SPECIFY. The default value is CENTROID.
        summationPoint
            A tuple of 3 floats specifying the summation point.
        componentResolution
            A SymbolicConstant specifying the component resolution. Possible values are
            NORMAL_TANGENTIAL and CSYS. The default value is NORMAL_TANGENTIAL.
        csysName
            A string specifying the name of the coordinate system.

        Returns
        -------
        FreeBody
            A FreeBody object.
        """
        ...

    @abaqus_method_doc
    def FreeBodyFromFaces(
        self,
        name: str,
        faces: str,
        summationLoc: Literal[C.SPECIFY, C.CENTROID, C.NODAL_AVERAGE] = CENTROID,
        summationPoint: tuple = (),
        componentResolution: Literal[C.NORMAL_TANGENTIAL, C.CSYS] = NORMAL_TANGENTIAL,
        csysName: str = "",
    ):
        """This method creates a FreeBody object and places it in the freeBodies repository.

        .. note::
            This function can be accessed by::

                session.FreeBodyFromEdges

        Parameters
        ----------
        name
            A string name for the free body.
        faces
            A DisplayGroup leaf object that specifies the physical constituents of the free body.
        summationLoc
            A SymbolicConstant specifying the location of the summation point. Possible values are
            CENTROID, NODAL_AVERAGE and SPECIFY. The default value is CENTROID.
        summationPoint
            A tuple of 3 floats specifying the summation point.
        componentResolution
            A SymbolicConstant specifying the component resolution. Possible values are
            NORMAL_TANGENTIAL and CSYS. The default value is NORMAL_TANGENTIAL.
        csysName
            A string specifying the name of the coordinate system.

        Returns
        -------
        FreeBody
            A FreeBody object.
        """
        ...

    @abaqus_method_doc
    def FreeBodyFromNodesElements(
        self,
        name: str,
        elements: str,
        nodes: str,
        summationLoc: Literal[C.SPECIFY, C.CENTROID, C.NODAL_AVERAGE] = CENTROID,
        summationPoint: tuple = (),
        componentResolution: Literal[C.NORMAL_TANGENTIAL, C.CSYS] = NORMAL_TANGENTIAL,
        csysName: str = "",
    ):
        """This method creates a FreeBody object and places it in the freeBodies repository.

        .. note::
            This function can be accessed by::

                session.FreeBodyFromEdges

        Parameters
        ----------
        name
            A string name for the free body.
        elements
            A DisplayGroup leaf object that specifies the physical constituents of the free body.
        nodes
            A DisplayGroup leaf object that specifies the physical constituents of the free body.
        summationLoc
            A SymbolicConstant specifying the location of the summation point. Possible values are
            CENTROID, NODAL_AVERAGE and SPECIFY. The default value is CENTROID.
        summationPoint
            A tuple of 3 floats specifying the summation point.
        componentResolution
            A SymbolicConstant specifying the component resolution. Possible values are
            NORMAL_TANGENTIAL and CSYS. The default value is NORMAL_TANGENTIAL.
        csysName
            A string specifying the name of the coordinate system.

        Returns
        -------
        FreeBody
            A FreeBody object.
        """
        ...

    @abaqus_method_doc
    def getFreeBodyData(
        self,
        step: int = 0,
        frame: int = 0,
        allActiveStepFrame: Boolean = OFF,
    ) -> Tuple[Tuple[Dict, ...], ...]:
        """This method returns the force and moment data of a FreeBody object.

        .. note::
            This function can be accessed by::

                session.freeBodies[name].getFreeBodyData

        .. versionadded:: 2025
            The ``getFreeBodyData`` method was added.

        Parameters
        ----------
        step
            An Int specifying the step from which to obtain values. The default value is the current step.
        frame
            An Int specifying the frame from which to obtain values. The default value is the current frame.
        allActiveStepFrame
            A Boolean specifying whether to obtain the values from the specified step and frame or from all active steps
            and frames.

        Returns
        -------
        tuple of tuple of dict
            A tuple of tuples of dictionaries, for each requested step and frame, containing the force and moment data.
        """
        ...
        return ()
