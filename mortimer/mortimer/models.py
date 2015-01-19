from django.db import models
from django.contrib.auth.models import User

class AppID(models.Model):
    app_user = models.ForeignKey(User)
    app_name = models.CharField(max_length=100)
    app_desc = models.CharField(max_length=500)

    class Meta:
        unique_together = (("app_user","app_name"),)

class AppData(models.Model):
    app_id = models.ForeignKey(AppID)
    username = models.CharField(max_length=25)
    enc_password = models.CharField(max_length=64)

    def as_json(self):
        return {
            'user':self.username,
            'pass': self.enc_password  # temporary!
            #pass=self.password
        }

    '''
    ToDo: Fix pycrypto installation bug
    def _get_password(self):
        enc_obj = AES.new( settings.SECRET_KEY )
        return u"%s" % enc_obj.decrypt( binascii.a2b_hex(self.enc_password) )

    def _get_ssn(self, pass_value):
        enc_obj = AES.new( settings.SECRET_KEY )
        self.enc_password = binascii.b2a_hex(enc_obj.encrypt( pass_value ))

    password = property(_get_password, _set_password)
    '''

    class Meta:
        unique_together = (("app_id","username"),)

