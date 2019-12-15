from odoo.fields import Selection, Char, Integer, Float, Text, Html


class SelectionYesNo(Selection):
  selection_yesno = [
                ('yes', 'Yes'),
                ('no', 'No')
              ]
  xml_size = 5

  def __init__(self, string='YesNo', **kwargs):
    super(SelectionYesNo, self).__init__(selection=self.selection_yesno,
                                         string=string,
                                         **kwargs)


class SelectionGender(Selection):
  selection_gender = [
                ('M', 'Male'),
                ('F', 'Female'),
                ('X', 'Other')
              ]
  xml_size = 1

  def __init__(self, selection=selection_gender, string='Gender', **kwargs):
    super(SelectionGender, self).__init__(selection=selection,
                                          string=string,
                                          **kwargs)


class CharName(Char):
  xml_size = 70

  def __init__(self, string='Name', **kwargs):
    kwargs['size'] = 70
    super(CharName, self).__init__(string=string, **kwargs)


class IntegerAge(Integer):
  xml_size = 3

  def __init__(self, string='Age', **kwargs):
    super().__init__(string, **kwargs)


class FloatLength(Float):
  total_decimal = (5, 2)
  xml_size = 5

  def __init__(self, string='Length', digits=total_decimal, **kwargs):
    super(Float, self).__init__(string=string, _digits=digits, **kwargs)
