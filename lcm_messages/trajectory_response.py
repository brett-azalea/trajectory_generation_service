"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class trajectory_response(object):
    __slots__ = ["timestamp", "control_points_size", "spline_order", "knot_points_size", "control_points", "knot_points"]

    __typenames__ = ["int64_t", "int32_t", "int32_t", "int32_t", "double", "double"]

    __dimensions__ = [None, None, None, None, ["control_points_size"], ["knot_points_size"]]

    def __init__(self):
        self.timestamp = 0
        self.control_points_size = 0
        self.spline_order = 0
        self.knot_points_size = 0
        self.control_points = []
        self.knot_points = []

    def encode(self):
        buf = BytesIO()
        buf.write(trajectory_response._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qiii", self.timestamp, self.control_points_size, self.spline_order, self.knot_points_size))
        buf.write(struct.pack('>%dd' % self.control_points_size, *self.control_points[:self.control_points_size]))
        buf.write(struct.pack('>%dd' % self.knot_points_size, *self.knot_points[:self.knot_points_size]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != trajectory_response._get_packed_fingerprint():
            raise ValueError("Decode error")
        return trajectory_response._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = trajectory_response()
        self.timestamp, self.control_points_size, self.spline_order, self.knot_points_size = struct.unpack(">qiii", buf.read(20))
        self.control_points = struct.unpack('>%dd' % self.control_points_size, buf.read(self.control_points_size * 8))
        self.knot_points = struct.unpack('>%dd' % self.knot_points_size, buf.read(self.knot_points_size * 8))
        return self
    _decode_one = staticmethod(_decode_one)

    def _get_hash_recursive(parents):
        if trajectory_response in parents: return 0
        tmphash = (0xb60999fc9d28ad51) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if trajectory_response._packed_fingerprint is None:
            trajectory_response._packed_fingerprint = struct.pack(">Q", trajectory_response._get_hash_recursive([]))
        return trajectory_response._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", trajectory_response._get_packed_fingerprint())[0]

