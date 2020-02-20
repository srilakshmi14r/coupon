def addtocart(request, prod_id):
        if (request.method == 'POST'):
                form = CartForm(request.POST)
                if form.is_valid():
                        newComment = form.save()
                        newComment.session = request.session.session_key[:20]
                        newComment.save()
                        return HttpResponseRedirect('/products/' + str(newComment.product.id))
        else:
                form = CartForm( {'name':'Your Name', 'session':'message', 'product':prod_id} )

        return render_to_response('Products/comment.html', {'form': form, 'prod_id': prod_id})

def delItem(request, prod_id):
        addtocart = get_object_or_404(Cart, pk = prod_id)
        prod_id = addtocart.product.id
        addtocart.delete()
        return HttpResponseRedirect('/userHistory/')


    def userHistory(request):
            promo = PromoCode.objects.filter(code = code_from_the_form)
            userCart = Cart.objects.filter(session = request.session.session_key[:20])
            totalCost = 0
            for item in userCart:
                    print item
                    totalCost += item.quantity * item.product.prodPrice * 1.06
            return render_to_response('Products/history.html', {'userCart':userCart, 'totalCost' : totalCost})
