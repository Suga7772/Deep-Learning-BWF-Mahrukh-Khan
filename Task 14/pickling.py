# https://docs.python.org/3/library/pickle.html#:~:text=“Pickling”%20is%20the%20process%20whereby,back%20into%20an%20object%20hierarchy.
# pickling helps in python object serialization
# “Pickling” is the process whereby a Python object
# hierarchy is converted into a byte stream, and
# “unpickling” is the inverse operation, whereby a
# byte stream (from a binary file or bytes-like object)
# is converted back into an object hierarchy.
import pickle


# https://www.synopsys.com/blogs/software-security/python-pickling/#:~:text=Pickle%20in%20Python%20is%20primarily,transport%20data%20over%20the%20network.
# while it all seems dandy , there are no effective ways to verify pickle streams
# being unpickled, remote code execution is a danger , to base on unencryption of network
# and data being modified.

# All in all, a secure connection between client is a surefire ways for the
# dangers of python pickling to be swept under the rug
# we can verify a pickle alteration (like checksum checks) using a cryptographic signature

# example of cryptographic signature
# pickled_data = pickle.dumps(data)
# digest =  hmac.new('shared-key', pickled_data, hashlib.sha1).hexdigest()
# header = '%s' % (digest)
# conn.send(header + ' ' + pickled_data)

# conn,addr = self.receiver_socket.accept()
# data = conn.recv(1024)
# recvd_digest, pickled_data = data.split(' ')
# new_digest = hmac.new('shared-key', pickled_data, hashlib.sha1).hexdigest()
# if recvd_digest != new_digest:
#     print 'Integrity check failed'
# else:
#     unpickled_data = pickle.loads(pickled_data)


class Foo:
    attr = 'a class attribute'

picklestring = pickle.dumps(Foo)


# there are certain benefits to pickling , for example in the case of actuators and mutators restriction on invokement
# If __getstate__() returns a false value, the __setstate__() method will not be called upon unpickling.

# video reference https://youtu.be/6wSFWOleZlc
