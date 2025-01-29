from accounts.models import CustomUser
from trainers.repositories import TrainerRepository


class TrainerService:
    @staticmethod
    def create_trainer(user_email, specialization):
        try:
            user = CustomUser.objects.get(email=user_email)  # Attempt to fetch the CustomUser by email
        except CustomUser.DoesNotExist:
            raise ValueError(f"CustomUser with email {user_email} does not exist.")  # Raise an error if not found

        return TrainerRepository.create_trainer(user, specialization)

    @staticmethod
    def update_trainer_profile(trainer, data):
        allowed_fields = {'profile_picture', 'bio', 'full_name'}
        filtered_data = {key: value for key, value in data.items() if key in allowed_fields}
        return TrainerRepository.update_trainer(trainer, filtered_data)

    @staticmethod
    def update_trainer_admin(trainer, data):
        disallowed_fields = {'profile_picture', 'bio', 'full_name', 'user'}
        filtered_data = {key: value for key, value in data.items() if key not in disallowed_fields}
        return TrainerRepository.update_trainer(trainer, filtered_data)

    @staticmethod
    def delete_trainer(trainer):
        TrainerRepository.delete_trainer(trainer)

    @staticmethod
    def list_all_trainers():
        return TrainerRepository.list_all()

    @staticmethod
    def get_trainer_by_user(user):
        """ Retrieve a trainer profile by the user (for logged-in trainer users) """
        return TrainerRepository.get_by_user(user)

    @staticmethod
    def get_trainer_by_id(trainer_id):
        """ Retrieve a trainer profile by id (for admin users) """
        return TrainerRepository.get_by_id(trainer_id)