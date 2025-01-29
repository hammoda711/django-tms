from trainers.models import Trainer


class TrainerRepository:
    @staticmethod
    def get_by_id(trainer_id):
        return Trainer.objects.filter(id=trainer_id).first()

    @staticmethod
    def get_by_user(user):
        return Trainer.objects.filter(user=user).first()

    @staticmethod
    def list_all():
        return Trainer.objects.all()

    @staticmethod
    def create_trainer(user, specialization):
        return Trainer.objects.create(user=user, specialization=specialization)

    @staticmethod
    def update_trainer(trainer, data):
        for field, value in data.items():
            setattr(trainer, field, value)
        trainer.save()
        return trainer

    @staticmethod
    def delete_trainer(trainer):
        trainer.delete()
