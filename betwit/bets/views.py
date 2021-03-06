from django.shortcuts import render

# Create your views here.

from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View

from user_profile.models import User
from matchs.models import Match
from models import Bet, BetCup
from forms import BetForm, BetCupForm


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

import logging
logger = logging.getLogger('django')


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)



class Index(View):
  def get(self, request):
    #return HttpResponse('I am called from a get Request')
    return render(request, 'base.html')
  def post(self, request):
    #return HttpResponse('I am called from a post Request')
    return render(request, 'base.html')

class UserRedirect(View):
  def get(self, request):
    if request.user.is_authenticated():
      logger.info('authorized user')
      return HttpResponseRedirect('/user/'+request.user.username)
    else:
      logger.info('unauthorized user')
      return HttpResponseRedirect('/login/')


class Profile(LoginRequiredMixin,View):
  """
  User profile reachable from /user/<username>/ URL
  """
  def get(self, request, username):
    params 	= dict()
    userProfile	= User.objects.get(username=username)
    bets 	= Bet.objects.filter(user=userProfile)
    form	= BetForm()
    params['bets'] = bets
    params['user'] = userProfile
    params['form'] = form
    return render(request, 'profile.html', params)

class PostBet(LoginRequiredMixin,View):
  def get(self, request, username):
    params              =  dict()
    user                = User.objects.get(username=username)
    form                = BetCupForm()
    params['user']      = user
    params['form']      = form
    return render(request, 'betcup.html', params)


  """ Match Post form available on page /user/<username> URL"""
  def post(self, request, username):
    form = BetForm(self.request.POST)
    if form.is_valid():
      ser	= User.objects.get(username=username)
      match     = Match.objects.get(id=form.cleaned_data['match'])
      print 'form = %r' % form
      bet	= Bet(
                    user 	= user,
                    match 	= match,
                    scoreA	= form.cleaned_data['scoreA'],
                    scoreB 	= form.cleaned_data['scoreB'],
                    triesA 	= form.cleaned_data['triesA'],
                    triesB 	= form.cleaned_data['triesB'],
                    card	= form.cleaned_data['card'],
                    drop_goal   = form.cleaned_data['drop_goal'],
                    fight       = form.cleaned_data['fight'],
                    created_date= timezone.now()
                  )
      bet.save()
      return HttpResponseRedirect('/user/'+username+'/')
    else:
      print 'form = %r' % form
      return render(request, 'betcup.html', {'form': form})


class PostBetCup(LoginRequiredMixin,View):
  def get(self, request, username):
    params		=  dict()
    user		= User.objects.get(username=username)
    form		= BetCupForm()
    params['user']	= user
    params['form']	= form
    return render(request, 'betcup.html', params)

  """
  Bet Cup Post form available on page /user/<username/betcup URL
  """
  def post(self, request, username):
    form = BetCupForm(self.request.POST)
    if form.is_valid():
      user	= User.objects.get(username=username)
      bet_cuup	= BetCup(
                    user	= user,
                    first	= form.cleaned_data['first'],
                    second      = form.cleaned_data['second'],
                    thrid       = form.cleaned_data['third'],
                    fourth      = form.cleaned_data['fourth'],
                    fifth       = form.cleaned_data['fifth'],
                    sixth       = form.cleaned_data['sixth'],
                    grand_slam	= form.cleaned_data['grand_slam'],
                    wooden_spoon= form.cleaned_data['wooden_spoon'],
                    created_date= timezone.now()
                  )
      bet_cup.save()
      return HttpResponseRedirect('/user/'+username+'/')
    else:
      return render(request,'betcup.html', {'form': form})

