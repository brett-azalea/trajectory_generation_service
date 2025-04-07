"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import lcm_azalea.UrRobotState

import lcm_azalea.RobotType

import lcm_azalea.NachiRobotState

class RobotState(object):
    __slots__ = ["robot_type", "nachi_robot_state_measured", "nachi_robot_state_desired", "ur_robot_state_measured", "ur_robot_state_desired"]

    __typenames__ = ["lcm_azalea.RobotType", "lcm_azalea.NachiRobotState", "lcm_azalea.NachiRobotState", "lcm_azalea.UrRobotState", "lcm_azalea.UrRobotState"]

    __dimensions__ = [None, None, None, None, None]

    def __init__(self):
        self.robot_type = lcm_azalea.RobotType()
        self.nachi_robot_state_measured = lcm_azalea.NachiRobotState()
        self.nachi_robot_state_desired = lcm_azalea.NachiRobotState()
        self.ur_robot_state_measured = lcm_azalea.UrRobotState()
        self.ur_robot_state_desired = lcm_azalea.UrRobotState()

    def encode(self):
        buf = BytesIO()
        buf.write(RobotState._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        assert self.robot_type._get_packed_fingerprint() == lcm_azalea.RobotType._get_packed_fingerprint()
        self.robot_type._encode_one(buf)
        assert self.nachi_robot_state_measured._get_packed_fingerprint() == lcm_azalea.NachiRobotState._get_packed_fingerprint()
        self.nachi_robot_state_measured._encode_one(buf)
        assert self.nachi_robot_state_desired._get_packed_fingerprint() == lcm_azalea.NachiRobotState._get_packed_fingerprint()
        self.nachi_robot_state_desired._encode_one(buf)
        assert self.ur_robot_state_measured._get_packed_fingerprint() == lcm_azalea.UrRobotState._get_packed_fingerprint()
        self.ur_robot_state_measured._encode_one(buf)
        assert self.ur_robot_state_desired._get_packed_fingerprint() == lcm_azalea.UrRobotState._get_packed_fingerprint()
        self.ur_robot_state_desired._encode_one(buf)

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != RobotState._get_packed_fingerprint():
            raise ValueError("Decode error")
        return RobotState._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = RobotState()
        self.robot_type = lcm_azalea.RobotType._decode_one(buf)
        self.nachi_robot_state_measured = lcm_azalea.NachiRobotState._decode_one(buf)
        self.nachi_robot_state_desired = lcm_azalea.NachiRobotState._decode_one(buf)
        self.ur_robot_state_measured = lcm_azalea.UrRobotState._decode_one(buf)
        self.ur_robot_state_desired = lcm_azalea.UrRobotState._decode_one(buf)
        return self
    _decode_one = staticmethod(_decode_one)

    def _get_hash_recursive(parents):
        if RobotState in parents: return 0
        newparents = parents + [RobotState]
        tmphash = (0x8fcfd849bc0363db+ lcm_azalea.RobotType._get_hash_recursive(newparents)+ lcm_azalea.NachiRobotState._get_hash_recursive(newparents)+ lcm_azalea.NachiRobotState._get_hash_recursive(newparents)+ lcm_azalea.UrRobotState._get_hash_recursive(newparents)+ lcm_azalea.UrRobotState._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if RobotState._packed_fingerprint is None:
            RobotState._packed_fingerprint = struct.pack(">Q", RobotState._get_hash_recursive([]))
        return RobotState._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", RobotState._get_packed_fingerprint())[0]

