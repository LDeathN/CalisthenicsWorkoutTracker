from django.core.exceptions import ValidationError
#from .models import Program


def validate_program_name(name):
    if not all(ch.isalpha() or ch == " " for ch in name):
        raise ValidationError('Program name must contain only letters!')

    #for program in Program.objects.all():
        #if program.name == name:
            #raise ValidationError('Program name is already taken!')
