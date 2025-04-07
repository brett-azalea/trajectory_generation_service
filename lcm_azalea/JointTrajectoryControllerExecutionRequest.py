"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import lcm_azalea.RobotType

import lcm_azalea.UrControlPoints

import lcm_azalea.NachiControlPoints

class JointTrajectoryControllerExecutionRequest(object):
    __slots__ = ["timestamp", "uuid", "robot_type", "control_points_size", "spline_order", "knot_points_size", "nachi_control_points", "ur_control_points", "knot_points"]

    __typenames__ = ["int64_t", "string", "lcm_azalea.RobotType", "int32_t", "int32_t", "int32_t", "lcm_azalea.NachiControlPoints", "lcm_azalea.UrControlPoints", "double"]

    __dimensions__ = [None, None, None, None, None, None, None, None, ["knot_points_size"]]

    def __init__(self):
        self.timestamp = 0
        self.uuid = ""
        self.robot_type = lcm_azalea.RobotType()
        self.control_points_size = 0
        self.spline_order = 0
        self.knot_points_size = 0
        self.nachi_control_points = lcm_azalea.NachiControlPoints()
        self.ur_control_points = lcm_azalea.UrControlPoints()
        self.knot_points = []

    def encode(self):
        buf = BytesIO()
        buf.write(JointTrajectoryControllerExecutionRequest._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">q", self.timestamp))
        __uuid_encoded = self.uuid.encode('utf-8')
        buf.write(struct.pack('>I', len(__uuid_encoded)+1))
        buf.write(__uuid_encoded)
        buf.write(b"\0")
        assert self.robot_type._get_packed_fingerprint() == lcm_azalea.RobotType._get_packed_fingerprint()
        self.robot_type._encode_one(buf)
        buf.write(struct.pack(">iii", self.control_points_size, self.spline_order, self.knot_points_size))
        assert self.nachi_control_points._get_packed_fingerprint() == lcm_azalea.NachiControlPoints._get_packed_fingerprint()
        self.nachi_control_points._encode_one(buf)
        assert self.ur_control_points._get_packed_fingerprint() == lcm_azalea.UrControlPoints._get_packed_fingerprint()
        self.ur_control_points._encode_one(buf)
        buf.write(struct.pack('>%dd' % self.knot_points_size, *self.knot_points[:self.knot_points_size]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != JointTrajectoryControllerExecutionRequest._get_packed_fingerprint():
            raise ValueError("Decode error")
        return JointTrajectoryControllerExecutionRequest._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = JointTrajectoryControllerExecutionRequest()
        self.timestamp = struct.unpack(">q", buf.read(8))[0]
        __uuid_len = struct.unpack('>I', buf.read(4))[0]
        self.uuid = buf.read(__uuid_len)[:-1].decode('utf-8', 'replace')
        self.robot_type = lcm_azalea.RobotType._decode_one(buf)
        self.control_points_size, self.spline_order, self.knot_points_size = struct.unpack(">iii", buf.read(12))
        self.nachi_control_points = lcm_azalea.NachiControlPoints._decode_one(buf)
        self.ur_control_points = lcm_azalea.UrControlPoints._decode_one(buf)
        self.knot_points = struct.unpack('>%dd' % self.knot_points_size, buf.read(self.knot_points_size * 8))
        return self
    _decode_one = staticmethod(_decode_one)

    def _get_hash_recursive(parents):
        if JointTrajectoryControllerExecutionRequest in parents: return 0
        newparents = parents + [JointTrajectoryControllerExecutionRequest]
        tmphash = (0x65e4f050acd092b4+ lcm_azalea.RobotType._get_hash_recursive(newparents)+ lcm_azalea.NachiControlPoints._get_hash_recursive(newparents)+ lcm_azalea.UrControlPoints._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if JointTrajectoryControllerExecutionRequest._packed_fingerprint is None:
            JointTrajectoryControllerExecutionRequest._packed_fingerprint = struct.pack(">Q", JointTrajectoryControllerExecutionRequest._get_hash_recursive([]))
        return JointTrajectoryControllerExecutionRequest._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", JointTrajectoryControllerExecutionRequest._get_packed_fingerprint())[0]

