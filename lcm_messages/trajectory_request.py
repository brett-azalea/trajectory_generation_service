"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import lcm_messages.pose

class trajectory_request(object):
    __slots__ = ["timestamp", "start_pose", "goal_pose"]

    __typenames__ = ["int64_t", "lcm_messages.pose", "lcm_messages.pose"]

    __dimensions__ = [None, None, None]

    def __init__(self):
        self.timestamp = 0
        self.start_pose = lcm_messages.pose()
        self.goal_pose = lcm_messages.pose()

    def encode(self):
        buf = BytesIO()
        buf.write(trajectory_request._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">q", self.timestamp))
        assert self.start_pose._get_packed_fingerprint() == lcm_messages.pose._get_packed_fingerprint()
        self.start_pose._encode_one(buf)
        assert self.goal_pose._get_packed_fingerprint() == lcm_messages.pose._get_packed_fingerprint()
        self.goal_pose._encode_one(buf)

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != trajectory_request._get_packed_fingerprint():
            raise ValueError("Decode error")
        return trajectory_request._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = trajectory_request()
        self.timestamp = struct.unpack(">q", buf.read(8))[0]
        self.start_pose = lcm_messages.pose._decode_one(buf)
        self.goal_pose = lcm_messages.pose._decode_one(buf)
        return self
    _decode_one = staticmethod(_decode_one)

    def _get_hash_recursive(parents):
        if trajectory_request in parents: return 0
        newparents = parents + [trajectory_request]
        tmphash = (0xecacc5d2916f99ba+ lcm_messages.pose._get_hash_recursive(newparents)+ lcm_messages.pose._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if trajectory_request._packed_fingerprint is None:
            trajectory_request._packed_fingerprint = struct.pack(">Q", trajectory_request._get_hash_recursive([]))
        return trajectory_request._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", trajectory_request._get_packed_fingerprint())[0]

