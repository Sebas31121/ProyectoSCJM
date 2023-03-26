def total_order(request):
    total = 0
    if request.user.is_authenticated:
        if "order " in request.session.keys:
            for key, value in request.session["order"].items():
                total += int(value["precio"])
    return{"total_order": total}
