# -*- coding: utf-8 -*-

from odoo import models, fields, api
from ..helpers import foobar_helper_field


class FooBar(models.Model):
    _name = 'foobar.foobar'

    name = fields.Char()
    name_custom = foobar_helper_field.CharName(string='Custom Name')

    age = fields.Integer()
    age_custom = foobar_helper_field.IntegerAge(string='Custom Age')

    length = fields.Float()
    length_custom = foobar_helper_field.FloatLength(string='Custom Float')

    question = fields.Selection(selection=[('yes', 'Yes'), ('no', 'No')], string='Question')
    question_custom = foobar_helper_field.SelectionYesNo(string='Custom Question')

    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    gender_custom = foobar_helper_field.SelectionGender(string='Custom Gender')
