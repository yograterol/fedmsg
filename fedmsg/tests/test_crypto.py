import os
import unittest

import fedmsg.crypto

SEP = os.path.sep
here = SEP.join(__file__.split(SEP)[:-1])


class TestCrypto(unittest.TestCase):

    def setUp(self):
        self.config = {
            # Normally this is /var/lib/puppet/ssl
            'ssldir': SEP.join((here, 'test_certs')),
            # Normally this is 'app01.stg.phx2.fedoraproject.org'
            'fqdn': 'test_cert',
        }

    def tearDown(self):
        self.config = None

    def test_full_circle(self):
        """ Try to sign and validate a message. """
        message = dict(msg='awesome')
        signed = fedmsg.crypto.sign(message, **self.config)
        assert fedmsg.crypto.validate(signed, **self.config)


if __name__ == '__main__':
    unittest.main()