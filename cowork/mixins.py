
class UserMixin(object):
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(UserMixin, self).dispatch(request, *args, **kwargs)
