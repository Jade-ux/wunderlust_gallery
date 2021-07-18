/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
    Credit to the Boutique Ado project
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"IBM Plex Sans", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#495057'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style, hidePostalCode: true});
card.mount('#card-element');

// Handle validation errors on the card input
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('payment-card-error');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times-circle"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle submit - from Boutique Ado project
var form = document.getElementById('checkout-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-btn').attr('disabled', true);
    $('#checkout-form').fadeToggle(100);
    $('#processing').fadeToggle(100);
    
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';    
    //The post method is an in-built- jQuery method
    //Wait for a response that the payment intent was updated
    //before calling the confirmed payment method
    //with the done() method
    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            address: {
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.town_or_city.value),
                country: $.trim(form.country.value),
                postal_code: $.trim(form.postcode.value),
                state: $.trim(form.county.value),
            }
        },
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('payment-card-error');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times-circle"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            $('#checkout-form').fadeToggle(100);
            $('#processing').fadeToggle(100);
            card.update({ 'disabled': false});
            $('#submit-btn').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
               form.submit();
            }
        }
    });
    }).fail(function () {
        // just reload the page, the error will be in django messages
        location.reload();
    })
});
