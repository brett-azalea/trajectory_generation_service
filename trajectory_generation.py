import numpy as np
from pydrake.all import (
    AddMultibodyPlantSceneGraph,
    BsplineTrajectory,
    DiagramBuilder,
    KinematicTrajectoryOptimization,
    MeshcatVisualizer,
    MeshcatVisualizerParams,
    Parser,
    PositionConstraint,
    Rgba,
    RigidTransform,
    Role,
    Solve,
    Sphere,
    StartMeshcat,
    SolverOptions,
    SnoptSolver,
    ClarabelSolver,
    CommonSolverOption,
    VisualizationConfig,
    ApplyVisualizationConfig,
    IpoptSolver,
    MinimumDistanceLowerBoundConstraint,
    CollisionFilterDeclaration,
    GeometrySet,
)

# TODOS
# 1. Create a subscriber for the LCM trajectory request
# 2



class TrajectoryGenerationService:
    def __init__(self):
        self.trajectory = None
        self.cached_trajectory_data = []


    def parse_lcm_message(self):
        pass
    
    def get_trajectory(self):
        return self.trajectory
    
    def read_trajectory_data(self):
        pass
    
    def generate_trajectory(self):
        pass
    