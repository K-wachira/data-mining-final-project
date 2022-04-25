from ._anvil_designer import formTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class form(formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_dropdowns()


    # Any code you write here will run when the form opens.

  def age_copy_6_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def work_experience_change(self, **event_args):
    """This method is called when an item is selected"""
    pass
  def get(self):
    return self.email.text
  def load_dropdowns(self):
    self.gender.items = ["Male", "Female"]
    self.education_level.items = ["Primary", "Highschool", "Diploma", "Degree or Higher"]
    self.father_alive.items = ["Yes", "No"]
    self.prev_scholarship.items = ["Yes", "No"]
    self.applicant_has_guardian.items = ["Yes", "No"]
    self.has_income.items = ["Yes", "No"]
    self.join_another_uni.items = ["Yes", "No"]
    self.marital_status.items = ["Single", "In a domestic Parnership"]
    self.mother_alive.items = ["Yes", "No"]
    self.neighbourhood.items = ["Slum", "Court", "Village", "Estate"]
    self.prev_student.items = ["Yes", "No"]
    self.rent_house.items = ["Yes", "No"]
    self.source.items = ["Partner", "None Parner"]
    self.work_experience.items = ["Yes", "No"]
    self.used_comp.items = ["Yes", "No"]
    self.tech_experience.items = ["Yes", "No"]
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.jsonData = {
      "email": self.email.text,
      "age": self.age.text,
      "gender": self.gender.selected_value,
      "education_level": self.education_level.selected_value,
      "father_alive": self.father_alive.selected_value,
      "prev_scholarship": self.prev_scholarship.selected_value, 
      "num_dependants": self.dependants_on_guadian.text,
      "has_guardian": self.applicant_has_guardian.selected_value,
      "has_income": self.has_income.selected_value,
      "another_university": self.join_another_uni.selected_value,
      "marital_status": self.marital_status.selected_value,
      "mother_alive": self.mother_alive.selected_value,
      "neighborhood": self.neighbourhood.selected_value,
      "no_siblings": self.siblings.text,
      "dependants": self.dependants.text,
      "prev_student": self.prev_student.selected_value,
      "rent": self.rent_house.selected_value,
      "source":self.source.selected_value,
      "tech_experience": self.tech_experience.selected_value,
      "used_comp": self.used_comp.selected_value,
      "work_experience": self.work_experience.selected_value
      
    }
    print(self.jsonData)
    self.result = anvil.server.call('load_data_colabs_', self.jsonData)[0]
    print(self.result)
    print(self.result["email"])
    print(self.result["recommendation"])
    print(self.result["reason"])

#     self.validator = validation.Validator()
#     self.label_to_display_if_invalid = "Input not correct"
#     self.validator.require_text_field(self.email.text, self.label_to_display_if_invalid)
#     self.validator.require_text_field(self.age.text, self.label_to_display_if_invalid)
#     self.validator.require_text_field(self.dependants_on_guadian.text, self.label_to_display_if_invalid)
#     self.validator.require_text_field(self.siblings.text, self.label_to_display_if_invalid)
#     self.validator.require_text_field(self.dependants.text, self.label_to_display_if_invalid)
      
    self.email_address.text = self.result["email"]
    self.recommendations_.text = self.result["recommendation"]
    self.reasons.text = self.result["reason"]
    print(self.email.text)
    print(self.gender.selected_value)
    pass


