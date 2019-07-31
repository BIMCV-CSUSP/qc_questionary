from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, StringField, RadioField
from wtforms.validators import DataRequired

class QuestionaryForm(FlaskForm):
    questionQC = "Which of the next MRI artifacts do you see in the image?"
    question_wrapping = BooleanField("Wrapping")
    question_fov_clipping = BooleanField("Fov clipping")
    question_ringing = BooleanField("Ringing")
    question_striping = BooleanField("Striping")
    question_blurring = BooleanField("Blurring")
    question_shadowed_arc = BooleanField("Shadowed arc")
    question_rf_noise = BooleanField("RF noise")
    question_spiking = BooleanField("Spiking")
    question_signal_loss = BooleanField("Signal loss")
    question_unexpected_inhomogeneity = BooleanField("Unexpected inhomogeneity")
    question_ghosting = BooleanField("Ghosting")
    question_motion_slice = BooleanField("Motion slice")
    question_unknown = BooleanField("Can't appreciate")


    submit = SubmitField('Send')

    def to_dict(self):
        dict={}
        dict["have_wrapping"]=self.question_wrapping.data
        dict["have_fov_clipping"]=self.question_fov_clipping.data
        dict["have_ringing"]=self.question_ringing.data
        dict["have_striping"]=self.question_striping.data
        dict["have_blurring"]=self.question_blurring.data
        dict["have_shadowed_arc"]=self.question_shadowed_arc.data
        dict["have_rf_noise"]=self.question_rf_noise.data
        dict["have_spiking"]=self.question_spiking.data
        dict["have_signal_loss"]=self.question_signal_loss.data
        dict["have_unexpected_inhomogeneity"]=self.question_unexpected_inhomogeneity.data
        dict["have_ghosting"]=self.question_ghosting.data
        dict["have_motion_slice"]=self.question_motion_slice.data
        dict["have_unknown"]=self.question_unknown.data
        return dict

    def get_header():
        return ["have_wrapping",
          "have_fov_clipping",
          "have_ringing",
          "have_striping",
          "have_blurring",
          "have_shadowed_arc",
          "have_rf_noise",
          "have_spiking",
          "have_signal_loss",
          "have_unexpected_inhomogeneity",
          "have_ghosting",
          "have_motion_slice",
          "have_unknown"]
