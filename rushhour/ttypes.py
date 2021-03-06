#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import *

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Road:
  """
  A road is recognized by its name and contains the length of the road from
  intersection to intersection in the variable Distance, along with the max
  speed that can be achieved on that road in addition to the current speed
  seen on that road. Last, it contains the names of the two intersections
  with which it connects.
  
  Attributes:
   - Name
   - Distance
   - MaxSpeed
   - CurrentSpeed
   - StartIntersection
   - EndIntersection
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'Name', None, None, ), # 1
    (2, TType.DOUBLE, 'Distance', None, None, ), # 2
    (3, TType.I32, 'MaxSpeed', None, None, ), # 3
    (4, TType.I32, 'CurrentSpeed', None, None, ), # 4
    (5, TType.STRING, 'StartIntersection', None, None, ), # 5
    (6, TType.STRING, 'EndIntersection', None, None, ), # 6
  )

  def __init__(self, Name=None, Distance=None, MaxSpeed=None, CurrentSpeed=None, StartIntersection=None, EndIntersection=None,):
    self.Name = Name
    self.Distance = Distance
    self.MaxSpeed = MaxSpeed
    self.CurrentSpeed = CurrentSpeed
    self.StartIntersection = StartIntersection
    self.EndIntersection = EndIntersection

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.Name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.DOUBLE:
          self.Distance = iprot.readDouble();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.MaxSpeed = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.CurrentSpeed = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.StartIntersection = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.EndIntersection = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Road')
    if self.Name != None:
      oprot.writeFieldBegin('Name', TType.STRING, 1)
      oprot.writeString(self.Name)
      oprot.writeFieldEnd()
    if self.Distance != None:
      oprot.writeFieldBegin('Distance', TType.DOUBLE, 2)
      oprot.writeDouble(self.Distance)
      oprot.writeFieldEnd()
    if self.MaxSpeed != None:
      oprot.writeFieldBegin('MaxSpeed', TType.I32, 3)
      oprot.writeI32(self.MaxSpeed)
      oprot.writeFieldEnd()
    if self.CurrentSpeed != None:
      oprot.writeFieldBegin('CurrentSpeed', TType.I32, 4)
      oprot.writeI32(self.CurrentSpeed)
      oprot.writeFieldEnd()
    if self.StartIntersection != None:
      oprot.writeFieldBegin('StartIntersection', TType.STRING, 5)
      oprot.writeString(self.StartIntersection)
      oprot.writeFieldEnd()
    if self.EndIntersection != None:
      oprot.writeFieldBegin('EndIntersection', TType.STRING, 6)
      oprot.writeString(self.EndIntersection)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Intersection:
  """
  An intersection is a node on the map with a name as well as a list of
  the roads with which it connects.
  
  Attributes:
   - Name
   - ConnectedRoads
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'Name', None, None, ), # 1
    (2, TType.LIST, 'ConnectedRoads', (TType.STRUCT,(Road, Road.thrift_spec)), None, ), # 2
  )

  def __init__(self, Name=None, ConnectedRoads=None,):
    self.Name = Name
    self.ConnectedRoads = ConnectedRoads

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.Name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.ConnectedRoads = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = Road()
            _elem5.read(iprot)
            self.ConnectedRoads.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Intersection')
    if self.Name != None:
      oprot.writeFieldBegin('Name', TType.STRING, 1)
      oprot.writeString(self.Name)
      oprot.writeFieldEnd()
    if self.ConnectedRoads != None:
      oprot.writeFieldBegin('ConnectedRoads', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.ConnectedRoads))
      for iter6 in self.ConnectedRoads:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class IntersectionsForRoad:
  """
  Wrapper struct referencing the two intersections connecting a Road.
  
  Attributes:
   - StartIntersection
   - EndIntersection
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'StartIntersection', (Intersection, Intersection.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'EndIntersection', (Intersection, Intersection.thrift_spec), None, ), # 2
  )

  def __init__(self, StartIntersection=None, EndIntersection=None,):
    self.StartIntersection = StartIntersection
    self.EndIntersection = EndIntersection

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.StartIntersection = Intersection()
          self.StartIntersection.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.EndIntersection = Intersection()
          self.EndIntersection.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('IntersectionsForRoad')
    if self.StartIntersection != None:
      oprot.writeFieldBegin('StartIntersection', TType.STRUCT, 1)
      self.StartIntersection.write(oprot)
      oprot.writeFieldEnd()
    if self.EndIntersection != None:
      oprot.writeFieldBegin('EndIntersection', TType.STRUCT, 2)
      self.EndIntersection.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class IntersectionsFromRoad:
  """
  Key: Road.Name
  Value: The two intersections connecting the given Road in form of the
  above struct.
  
  Attributes:
   - Connections
  """

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'Connections', (TType.STRING,None,TType.STRUCT,(IntersectionsForRoad, IntersectionsForRoad.thrift_spec)), None, ), # 1
  )

  def __init__(self, Connections=None,):
    self.Connections = Connections

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.MAP:
          self.Connections = {}
          (_ktype8, _vtype9, _size7 ) = iprot.readMapBegin() 
          for _i11 in xrange(_size7):
            _key12 = iprot.readString();
            _val13 = IntersectionsForRoad()
            _val13.read(iprot)
            self.Connections[_key12] = _val13
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('IntersectionsFromRoad')
    if self.Connections != None:
      oprot.writeFieldBegin('Connections', TType.MAP, 1)
      oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.Connections))
      for kiter14,viter15 in self.Connections.items():
        oprot.writeString(kiter14)
        viter15.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class RoadMap:
  """
  This is the main Map which contains a set of all intersections
  (and thus roads) on the map.
  
  Attributes:
   - Intersections
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'Intersections', (TType.STRUCT,(Intersection, Intersection.thrift_spec)), None, ), # 1
  )

  def __init__(self, Intersections=None,):
    self.Intersections = Intersections

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.Intersections = []
          (_etype19, _size16) = iprot.readListBegin()
          for _i20 in xrange(_size16):
            _elem21 = Intersection()
            _elem21.read(iprot)
            self.Intersections.append(_elem21)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('RoadMap')
    if self.Intersections != None:
      oprot.writeFieldBegin('Intersections', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.Intersections))
      for iter22 in self.Intersections:
        iter22.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class NoMoveMadeException(Exception):
  """
  This exception is thrown if a call to getRoadConditions is
  is made before canMove() is verified, when takeRoad is called
  with a speed greater than the CurrentSpeed or when takeRoad
  is supplied with a road that is not present at current intersection.
  
  Attributes:
   - message
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
  )

  def __init__(self, message=None,):
    self.message = message

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('NoMoveMadeException')
    if self.message != None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class GameOverException(Exception):
  """
  Thrown if any call to canMove() or takeRoad() is called after game is won.
  """

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('GameOverException')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class UnregisteredException(Exception):
  """
  Thrown if any calls are made to any gameplay functions before registering
  or joining the game.
  """

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('UnregisteredException')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class DuplicateEmailException(Exception):
  """
  Thrown when a player attempts to register using an email that is
  already registered in a particular game.
  """

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('DuplicateEmailException')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

