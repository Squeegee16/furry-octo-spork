from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,BooleanField, SubmitField, FloatField, SubmitField, TextAreaField, DateField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired,NumberRange,length, EqualTo, Email

class editplantdata(FlaskForm):
	epdhardiness = StringField('Hardiness Type           ')
	epdplantdate = StringField('Reccomended Planting Date')
	epdDTM = IntegerField('Days to Maturity         ', validators=[NumberRange(min=-1, max=1095)])
	epdgermination = IntegerField('Germination Time in days ', validators=[NumberRange(min=-1, max=180)])
	epdsowtype = StringField('Direct Sow or Transplantable?')
	epdseeddepth = FloatField('Sowing Depth in inches     ')
	epdseedspacemin = FloatField('Minimum Seed spacing inches')
	epdseedspacemax = FloatField('Maximum Seed spacing inches')
	epdrowspacemin = FloatField('Minimum Row spacing inches ')
	epdrowspacemax = FloatField('Maximum Row spacing inches ')
	epdfamilyCabbage =BooleanField('Cabbage Family') 
	epdfamilyCarrot =BooleanField('Carrot Family') 
	epdfamilyCelery =BooleanField('Celery Family') 
	epdfamilyBean =BooleanField('Bean Family') 
	epdfamilyBeet =BooleanField('Beet Family') 
	epdfamilyOnion =BooleanField('Onion Family')
	epdfamilyPea =BooleanField('Pea Family') 
	epdfamilyPepper =BooleanField('Pepper Family') 
	epdfamilyPotato =BooleanField('Potato Family') 
	epdfamilySquash =BooleanField('Squash Family')
	epdfamilyTomato =BooleanField('Tomato Family')  
	epdpic = FileField('Update Plant Picture', validators=[FileAllowed(['jpg', 'png'])])
	epdsubmit = SubmitField('Save Changes')

