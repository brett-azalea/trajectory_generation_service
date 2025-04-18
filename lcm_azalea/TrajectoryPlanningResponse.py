"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class TrajectoryPlanningResponse(object):
    __slots__ = ["timestamp", "uuid", "success", "status", "dof", "spline_order", "control_points_size", "knot_points_size", "control_points", "knot_points"]

    __typenames__ = ["int64_t", "string", "boolean", "string", "int16_t", "int16_t", "int32_t", "int32_t", "double", "double"]

    __dimensions__ = [None, None, None, None, None, None, None, None, ["control_points_size", "dof"], ["knot_points_size"]]

    def __init__(self):
        self.timestamp = 0
        self.uuid = ""
        self.success = False
        self.status = ""
        self.dof = 0
        self.spline_order = 0
        self.control_points_size = 0
        self.knot_points_size = 0
        self.control_points = []
        self.knot_points = []

    def encode(self):
        buf = BytesIO()
        buf.write(TrajectoryPlanningResponse._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">q", self.timestamp))
        __uuid_encoded = self.uuid.encode('utf-8')
        buf.write(struct.pack('>I', len(__uuid_encoded)+1))
        buf.write(__uuid_encoded)
        buf.write(b"\0")
        buf.write(struct.pack(">b", self.success))
        __status_encoded = self.status.encode('utf-8')
        buf.write(struct.pack('>I', len(__status_encoded)+1))
        buf.write(__status_encoded)
        buf.write(b"\0")
        buf.write(struct.pack(">hhii", self.dof, self.spline_order, self.control_points_size, self.knot_points_size))
        for i0 in range(self.control_points_size):
            buf.write(struct.pack('>%dd' % self.dof, *self.control_points[i0][:self.dof]))
        buf.write(struct.pack('>%dd' % self.knot_points_size, *self.knot_points[:self.knot_points_size]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != TrajectoryPlanningResponse._get_packed_fingerprint():
            raise ValueError("Decode error")
        return TrajectoryPlanningResponse._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = TrajectoryPlanningResponse()
        self.timestamp = struct.unpack(">q", buf.read(8))[0]
        __uuid_len = struct.unpack('>I', buf.read(4))[0]
        self.uuid = buf.read(__uuid_len)[:-1].decode('utf-8', 'replace')
        self.success = bool(struct.unpack('b', buf.read(1))[0])
        __status_len = struct.unpack('>I', buf.read(4))[0]
        self.status = buf.read(__status_len)[:-1].decode('utf-8', 'replace')
        self.dof, self.spline_order, self.control_points_size, self.knot_points_size = struct.unpack(">hhii", buf.read(12))
        self.control_points = []
        for i0 in range(self.control_points_size):
            self.control_points.append(struct.unpack('>%dd' % self.dof, buf.read(self.dof * 8)))
        self.knot_points = struct.unpack('>%dd' % self.knot_points_size, buf.read(self.knot_points_size * 8))
        return self
    _decode_one = staticmethod(_decode_one)

    def _get_hash_recursive(parents):
        if TrajectoryPlanningResponse in parents: return 0
        tmphash = (0x881b5e75154c560f) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if TrajectoryPlanningResponse._packed_fingerprint is None:
            TrajectoryPlanningResponse._packed_fingerprint = struct.pack(">Q", TrajectoryPlanningResponse._get_hash_recursive([]))
        return TrajectoryPlanningResponse._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", TrajectoryPlanningResponse._get_packed_fingerprint())[0]

