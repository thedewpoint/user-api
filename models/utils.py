# https://stackoverflow.com/a/10370224/2162857
class Serializable:
    def to_dict(self):
        dictret = dict(self.__dict__)
        dictret.pop('_sa_instance_state', None)
        return dictret
