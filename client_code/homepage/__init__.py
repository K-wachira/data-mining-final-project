from ._anvil_designer import homepageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import plotly.graph_objects as go
import plotly as px
#!/usr/bin/env python3
from .form import form
from collections import Counter

class homepage(homepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.on = False
    self.file = None
    self.result = None
    # Any code you write here will run when the form opens.
    user = anvil.users.login_with_form() 
    self.hide_components()
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.file:
        self.results = anvil.server.call('load_data_colab_', self.file) # Collab
        #self.results = anvil.server.call('load_data', self.file)  # Deepnote
    else:
        self.error_handler("Warning: No data uploaded")
    if type(self.results) == list:
      self.repeating_panel_1.items = self.results
      # plot the graphs
      self.plot_report_a()
      self.plot_report_b() 

      self.show_components()
    elif type(self.results) == str:
      if self.results == "AttributeError":
        self.error_handler("Warning: The file uploaded does not follow expected structure.\n Please Download and use the provided template")
      else:
        self.error_handler("Warning: File uploaded is not a csv file")

        
        
    # clear what has been selected as file
    
    pass

  def plot_report_a(self, **event_args):
    """This method is called when the Plot is shown on the screen"""
    self.rejected = 0 
    self.admitted = 0 
    for result in self.results:
      if Admit in result["recommendation"]:
        self.admitted +=1
      else:
        self.rejected +=1 
      
    self.plot_a.data = go.Bar(x = ["Admited", "Rejected"],
                              y = [self.admitted, self.rejected ],
                              marker=dict(color='#2196f3'))
    self.style_plot(self.plot_a)
    self.plot_a.layout.title = "Admitted Vs Rejected Applicants"
    self.plot_a.layout.yaxis.title = "Applicant Count"
    pass
  def plot_report_b(self, **event_args):
    """This method is called when the Plot is shown on the screen"""
    reasons = []
    for result in self.results:
      if len(result["reason"]) > 0:
        reasons.extend(result["reason"])
    dicti = Counter(reasons)
    res = []
    count = []
    for k, v in dicti.items():
      res.append(k)
      count.append(v)
    print(res, count)
    self.plot_b.data = go.Bar(x = res,
                              y = count,
                              marker=dict(color='#D4D5CD'))
    self.style_plot(self.plot_b)
    self.plot_b.layout.title = "Reason for Applicants rejections"
    self.plot_b.layout.yaxis.title = "Number of Rejections"
    pass
  def error_handler(self, err):
    alert(str(err), title="An error has occurred")
    pass
  

  def file_loader_1_change(self, file, **event_args ):
      self.file = file
    
    
  def hide_components(self):
    self.data_grid_1.visible = False
    self.plot_a.visible = False
    self.plot_b.visible = False
    self.report.visible = False
  def show_components(self):
    self.data_grid_1.visible = True
    self.plot_a.visible = True
    self.plot_b.visible = True
    

    self.report.visible = True

  def style_plot(self, plot):
    # expand the graphs
    plot.layout = go.Layout(
        margin=dict(
            l=50, #left margin
            r=50, #right margin
            b=50, #bottom margin
            t=50, #top margin
        ),
        font=dict(family='Arial', size=10),
        xaxis=dict(
          zeroline=False,
          tickfont=dict(
              family='Arial',
              size=11,
              color='#808080'
          ),
        ),
        yaxis=dict(
            zeroline=False,
            tickfont=dict(
                family='Arial',
                size=11,
                color='#808080'
            ),
        ))
  def plot_a_click(self, **event_args ):
    pass
  def repeating_panel_1_show(self, **event_args ):
    pass
  def template_click(self, **event_args ):
    pass
  def data_grid_1_show(self, **event_args ):
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    print("start" )
    
    if self.on == False:
      self.card_1.add_component(form())
      self.submit.visible = False

      self.on = True 
    elif self.on == True:
      print("Hiding")
      self.card_1.clear()
      self.on =False
      self.submit.visible = True
    print(self.on)

    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.file_loader_1.clear()

  def single_submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    print("Single Submit")
    pass

  def pipe_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.error_handler("API Key Error. Kindly refresh your page or contact surveryMokeyapply support team.")
    pass















