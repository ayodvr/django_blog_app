from django import forms 
import re
from carApp.models import Contact, BoldLinks

class ContactForm(forms.ModelForm):

    class Meta:
        model  = Contact
        fields = "__all__"

        labels = {
            
            'fullname': ("Your Fullname"),
            'email': ("Your Email"),
            'message': ("Your Message")
        }
        widgets = {

            'message':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter your message'}),
        }

class StudentForm(forms.Form):

        State_List = [
            ('State', 'State'),
            ('Akwa Ibom','Akwa Ibom'),
            ('Anambra',	'Anambra'),
            ('Bauchi',	'Bauchi'),
            ('Bayelsa',	'Bayelsa'),
            ('Benue',	'Benue')
        ]

        Course_List = [
            ('Course/Duration', 'Course/Duration'),
            ('Python/Django(6 months)','Python/Django (6 months)'),
            ('PHP/Laravel(6 months)','PHP/Laravel (6 months)'),
            ('C#/DotNet(6 months)','C#/DotNet (6 months)'),
            ('CMS/Wordpress(6 months)','CMS/Wordpress (6 months)')
        ]
        student = forms.CharField(required=False,
                                    label="Fullname",
                                    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}))

        email = forms.CharField(required=False,
                                    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your email'}))

        phone = forms.CharField(required=False,
                                    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your phone number'}))

        address = forms.CharField(required=False,
                                    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your address'}))

        state = forms.CharField(required=False,
                                    widget=forms.Select(choices=State_List))

        course = forms.CharField(required=False,
                                    widget=forms.Select(choices=Course_List))

        enrollment_date = forms.DateField(required=False,
                                    widget=forms.DateInput(attrs={'class': 'form-control datepicker'}))

        graduation_date = forms.DateTimeField(required=False,
                                    widget=forms.DateInput(attrs={'class': 'form-control datepicker'}))


    # fullname    = forms.CharField(required=False,
    #                                 label="Your Fullname",
    #                                 widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your fullname'})
    #                             )

    # email       = forms.EmailField(required=False,
    #                                 label="Your Email",
    #                                 widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your email'})
    #                             )

    # message     = forms.CharField(required=False,
    #                                 label="Your Message",
    #                                 widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter your message'})
    #                             )


        # def clean_student(self):
        #     student = self.cleaned_data["student"]

        #     if student == "":
        #         raise forms.ValidationError("Fullname can not be empty")
            
        #     if len(student) < 5:
        #         raise forms.ValidationError("Fullname should be more than 5 xters")

        #     return fullname

        # def clean_email(self):
        #     email = self.cleaned_data["email"]

        #     if email == "":
        #         raise forms.ValidationError("Email can not be empty")

        #     return email

        def clean(self):
            super(StudentForm, self).clean()

            name      = self.cleaned_data['student']
            mail      = self.cleaned_data['email']
            phone     = self.cleaned_data['phone']
            address   = self.cleaned_data['address']
            state     = self.cleaned_data['state']
            crs       = self.cleaned_data['course']
            enr       = self.cleaned_data['enrollment_date']
            grad      = self.cleaned_data['graduation_date']

            mailFormat = r"(^[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+$)"
            num = r"^[-+]?[0-11]+$"
            phoneFormat = r"(\(\d{3}\) \d{3}-\d{5})"

            if name == "":
                self._errors["student"] = self.error_class(["Fullname can't be empty"])

            if mail == "":
                self._errors["email"] = self.error_class(["Email can't be empty"])
            elif not re.search(mailFormat, mail):
                self._errors["email"] = self.error_class(["Invalid Email"])

            if phone == "":
                self._errors["phone"] = self.error_class(["Please enter your phone number"])
            elif not re.search(num, phone):
                self.errors["phone"] = self.error_class(["Only digits are allowed"])
            elif not re.search(phoneFormat,phone):
                self.errors["phone"] = self.error_class(["Invalid phone number format"])

            if address == "":
                self._errors["address"] = self.error_class(["Please enter your address"])

            if state == state[0]:
                self._errors["state"] = self.error_class(["Please select your state"])

            if crs == crs[0]:
                self._errors["course"] = self.error_class(["Please select your course"])

            if enr == "":
                self._errors["enrollment_date"] = self.error_class(["Choose enrollment date"])

            if grad == "":
                self._errors["graduation_date"] = self.error_class(["Choose graduation date"])

            return self.cleaned_data

