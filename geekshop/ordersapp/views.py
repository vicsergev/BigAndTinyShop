from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.forms import inlineformset_factory

from ordersapp.models import Order, OrderItem
from ordersapp.forms import OrderItemForm


class OrdersList(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderCreate(CreateView):
    model = Order
    fields = []
    success_url = reverse_lazy('order:orders_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        if self.request.POST:
            OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)
            formset = OrderFormSet(self.request.POST, self.request.FILES)
        else:
            basket_items = self.request.user.basket.all()
            if len(basket_items):
                OrderFormSet = inlineformset_factory(Order, OrderItem, \
                    form=OrderItemForm, extra=len(basket_items))

                formset = OrderFormSet()
                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_items[num].product
                    form.initial['quantity'] = basket_items[num].quantity
            else:
                OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)
                formset = OrderFormSet()

        data['orderitems'] = formset
        return data