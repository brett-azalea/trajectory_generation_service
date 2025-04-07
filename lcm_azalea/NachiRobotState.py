"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import lcm_azalea.NachiJointAngles

class NachiRobotState(object):
    __slots__ = ["joint_angles", "motor_current", "emergency_stop", "latency", "message_number"]

    __typenames__ = ["lcm_azalea.NachiJointAngles", "double", "boolean", "double", "int32_t"]

    __dimensions__ = [None, [8], None, None, None]

    def __init__(self):
        self.joint_angles = lcm_azalea.NachiJointAngles()
        self.motor_current = [ 0.0 for dim0 in range(8) ]
        self.emergency_stop = False
        self.latency = 0.0
        self.message_number = 0

    def encode(self):
        buf = BytesIO()
        buf.write(NachiRobotState._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        assert self.joint_angles._get_packed_fingerprint() == lcm_azalea.NachiJointAngles._get_packed_fingerprint()
        self.joint_angles._encode_one(buf)
        buf.write(struct.pack('>8d', *self.motor_current[:8]))
        buf.write(struct.pack(">bdi", self.emergency_stop, self.latency, self.message_number))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != NachiRobotState._get_packed_fingerprint():
            raise ValueError("Decode error")
        return NachiRobotState._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = NachiRobotState()
        self.joint_angles = lcm_azalea.NachiJointAngles._decode_one(buf)
        self.motor_current = struct.unpack('>8d', buf.read(64))
        self.emergency_stop = bool(struct.unpack('b', buf.read(1))[0])
        self.latency, self.message_number = struct.unpack(">di", buf.read(12))
        return self
    _decode_one = staticmethod(_decode_one)

    def _get_hash_recursive(parents):
        if NachiRobotState in parents: return 0
        newparents = parents + [NachiRobotState]
        tmphash = (0xd55167c7b43716f4+ lcm_azalea.NachiJointAngles._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if NachiRobotState._packed_fingerprint is None:
            NachiRobotState._packed_fingerprint = struct.pack(">Q", NachiRobotState._get_hash_recursive([]))
        return NachiRobotState._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", NachiRobotState._get_packed_fingerprint())[0]

