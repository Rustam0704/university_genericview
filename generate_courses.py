import random

from faker import Faker

faker = Faker()


def fake_test():
    Degree = [
        ("master", "Master"),
        ("bachelor", "Bachelor"),
        ("academic", "Academic"),
        ("drscience", "DrScience"),
        ("phs", "PhD"),
    ]
    # print(random.choice(Degree))


# print(faker.book())


def main():
    Degree = [
        ("master", "Master"),
        ("bachelor", "Bachelor"),
        ("academic", "Academic"),
        ("drscience", "DrScience"),
        ("phs", "PhD"),
    ]

    for _ in range(25):
        # Teacher.objects.create(first_name=faker.first_name(), last_name=faker.last_name(), age=random.randint(25, 55),
        #                        email=faker.email(), degree=random.choice(Degree))
        # spec=Speciality.objects.create(name=faker.job(), is_active=random.choice([True, False]), start_date=faker.date())
        # spec.slug=f'{spec.name}-{spec.start_date}'
        # spec.save()

        subj = Subject.objects.create(name=faker.job(), teacher=Teacher.objects.get(id=random.randint(102, 128)))
        for j in range(random.randint(1, 5)):
            spec = Speciality.objects.get(id=random.randint(31, 55))
            subj.speciality.add(spec)
        subj.save()


if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "university.settings")
    application = get_wsgi_application()

    from courses.models import Speciality, Teacher, Subject

    main()
    # fake_test()
