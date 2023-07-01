# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from vehicle_msgs/Lane.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class Lane(genpy.Message):
  _md5sum = "34fa6f4e572e18530e0aa845f18bc92d"
  _type = "vehicle_msgs/Lane"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header

int32 id
int32 dir

int32[] child_id
int32[] father_id

int32 l_lane_id
bool l_change_avbl

int32 r_lane_id
bool r_change_avbl

string behavior

float32 length

geometry_msgs/Point start_point
geometry_msgs/Point final_point

geometry_msgs/Point[] points

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
"""
  __slots__ = ['header','id','dir','child_id','father_id','l_lane_id','l_change_avbl','r_lane_id','r_change_avbl','behavior','length','start_point','final_point','points']
  _slot_types = ['std_msgs/Header','int32','int32','int32[]','int32[]','int32','bool','int32','bool','string','float32','geometry_msgs/Point','geometry_msgs/Point','geometry_msgs/Point[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,id,dir,child_id,father_id,l_lane_id,l_change_avbl,r_lane_id,r_change_avbl,behavior,length,start_point,final_point,points

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Lane, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.id is None:
        self.id = 0
      if self.dir is None:
        self.dir = 0
      if self.child_id is None:
        self.child_id = []
      if self.father_id is None:
        self.father_id = []
      if self.l_lane_id is None:
        self.l_lane_id = 0
      if self.l_change_avbl is None:
        self.l_change_avbl = False
      if self.r_lane_id is None:
        self.r_lane_id = 0
      if self.r_change_avbl is None:
        self.r_change_avbl = False
      if self.behavior is None:
        self.behavior = ''
      if self.length is None:
        self.length = 0.
      if self.start_point is None:
        self.start_point = geometry_msgs.msg.Point()
      if self.final_point is None:
        self.final_point = geometry_msgs.msg.Point()
      if self.points is None:
        self.points = []
    else:
      self.header = std_msgs.msg.Header()
      self.id = 0
      self.dir = 0
      self.child_id = []
      self.father_id = []
      self.l_lane_id = 0
      self.l_change_avbl = False
      self.r_lane_id = 0
      self.r_change_avbl = False
      self.behavior = ''
      self.length = 0.
      self.start_point = geometry_msgs.msg.Point()
      self.final_point = geometry_msgs.msg.Point()
      self.points = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2i().pack(_x.id, _x.dir))
      length = len(self.child_id)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.child_id))
      length = len(self.father_id)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.father_id))
      _x = self
      buff.write(_get_struct_iBiB().pack(_x.l_lane_id, _x.l_change_avbl, _x.r_lane_id, _x.r_change_avbl))
      _x = self.behavior
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_f6d().pack(_x.length, _x.start_point.x, _x.start_point.y, _x.start_point.z, _x.final_point.x, _x.final_point.y, _x.final_point.z))
      length = len(self.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.points:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.start_point is None:
        self.start_point = geometry_msgs.msg.Point()
      if self.final_point is None:
        self.final_point = geometry_msgs.msg.Point()
      if self.points is None:
        self.points = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.id, _x.dir,) = _get_struct_2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.child_id = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.father_id = s.unpack(str[start:end])
      _x = self
      start = end
      end += 10
      (_x.l_lane_id, _x.l_change_avbl, _x.r_lane_id, _x.r_change_avbl,) = _get_struct_iBiB().unpack(str[start:end])
      self.l_change_avbl = bool(self.l_change_avbl)
      self.r_change_avbl = bool(self.r_change_avbl)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.behavior = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.behavior = str[start:end]
      _x = self
      start = end
      end += 52
      (_x.length, _x.start_point.x, _x.start_point.y, _x.start_point.z, _x.final_point.x, _x.final_point.y, _x.final_point.z,) = _get_struct_f6d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.points = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.points.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2i().pack(_x.id, _x.dir))
      length = len(self.child_id)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.child_id.tostring())
      length = len(self.father_id)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.father_id.tostring())
      _x = self
      buff.write(_get_struct_iBiB().pack(_x.l_lane_id, _x.l_change_avbl, _x.r_lane_id, _x.r_change_avbl))
      _x = self.behavior
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_f6d().pack(_x.length, _x.start_point.x, _x.start_point.y, _x.start_point.z, _x.final_point.x, _x.final_point.y, _x.final_point.z))
      length = len(self.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.points:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.start_point is None:
        self.start_point = geometry_msgs.msg.Point()
      if self.final_point is None:
        self.final_point = geometry_msgs.msg.Point()
      if self.points is None:
        self.points = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.id, _x.dir,) = _get_struct_2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.child_id = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.father_id = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      _x = self
      start = end
      end += 10
      (_x.l_lane_id, _x.l_change_avbl, _x.r_lane_id, _x.r_change_avbl,) = _get_struct_iBiB().unpack(str[start:end])
      self.l_change_avbl = bool(self.l_change_avbl)
      self.r_change_avbl = bool(self.r_change_avbl)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.behavior = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.behavior = str[start:end]
      _x = self
      start = end
      end += 52
      (_x.length, _x.start_point.x, _x.start_point.y, _x.start_point.z, _x.final_point.x, _x.final_point.y, _x.final_point.z,) = _get_struct_f6d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.points = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.points.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2i = None
def _get_struct_2i():
    global _struct_2i
    if _struct_2i is None:
        _struct_2i = struct.Struct("<2i")
    return _struct_2i
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_f6d = None
def _get_struct_f6d():
    global _struct_f6d
    if _struct_f6d is None:
        _struct_f6d = struct.Struct("<f6d")
    return _struct_f6d
_struct_iBiB = None
def _get_struct_iBiB():
    global _struct_iBiB
    if _struct_iBiB is None:
        _struct_iBiB = struct.Struct("<iBiB")
    return _struct_iBiB