from django import forms


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class CouponApplyForm(forms.Form):
    code = forms.CharField()
    code.widget.attrs.update({'class': INPUT_CLASSES})
