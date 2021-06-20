class BaseUser:
    pass


class Admin(BaseUser):
    pass


class Patient(BaseUser):
    pass


class HospitalWorker(BaseUser):
    pass


class Doctor(HospitalWorker):
    pass


class ServiceForce(HospitalWorker):
    pass


class Nurse(HospitalWorker):
    pass
