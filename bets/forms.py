from django.forms import ModelForm, Textarea
from django import forms
from bets.models import MatchBet,TournamentBet, BetPoint
from tournaments.models import Match
from django.utils import timezone

class MatchBetForm( ModelForm ):
    """
    MatchBet form to place a bet on a match
    """
    #matchs              = Match.objects.filter(date__gte=timezone.now())
    def __init__( self, *args, **kwargs ):
        mid = kwargs.pop( 'match_id', None)
        tid = kwargs.pop( 'tournament_id', None)
        # check if match is available for betting
        # if match_id is not None, limit choice to that match
        # else limit choice to only available match (match.date > timezone.now()
        choice = [(None, '-- choose a match --'), ]
        # this is in case we present a form where user can bet on every available match
        choice = forms.ModelChoiceField(queryset=Match.objects.filter( date__gte = timezone.now() ) )
        # if mid defined, this is because user used /mbet_add/tid/match/mid
        if mid is not None:
            choice = forms.ModelChoiceField(queryset=Match.objects.filter( id = mid ) )
        # if tid defined, this is beacause user used /mbet_add/tid
        if tid is not None:
            choice  = forms.ModelChoiceField( queryset = Match.objects.filter( tournament_id = tid ).filter( date__gte = timezone.now() ) )
        super( MatchBetForm, self ).__init__( *args, **kwargs )
        self.fields['match_id'] = choice

    class Meta:
        model   = MatchBet
        exclude = ['player_id', 'points_won']

class TournamentBetForm( ModelForm ):
    """
    TournamentBet form which will be closed at the begining of the first match
    """
#    teams   = [(None, '-- choose a team --'), ]
#    first_team  = forms.ChoiceField(
#                choices = teams,
#                initial = (None, '-- choose a match --'),
#                required= True )
#    second_team  = forms.ChoiceField(
#                choices = teams,
#                initial = (None, '-- choose a match --'),
#                required= True )
#    third_team  = forms.ChoiceField(
#                choices = teams,
#                initial = (None, '-- choose a match --'),
#                required= True )
#    fourth_team  = forms.ChoiceField(
#                choices = teams,
#                initial = (None, '-- choose a match --'),
#                required= True )
#    fifth_team  = forms.ChoiceField(
#                choices = teams,
#                initial = (None, '-- choose a match --'),
#                required= True )
#    sixth_team  = forms.ChoiceField(
#                choices = teams,
#                initial = (None, '-- choose a match --'),
#                required= True )

    # TODO get every team name of the tournament
    def __init__( self, *args, **kwargs):
        tid     = kwargs.pop( 'tournament_id', None)
        teams   = [(None, '-- choose a team --'), ]
        if tid is not None:
            matchs  = Match.objects.filter( tournament_id = tid )
            for m in matchs:
                t = (m.home_team_id.name, m.home_team_id.name)
                if t not in teams:
                    teams.append(t)
                t = (m.away_team_id.name, m.away_team_id.name )
                if t not in teams:
                   teams.append(t) 

        super(TournamentBetForm, self).__init__(*args, **kwargs)
        self.fields['first_team'] = forms.ChoiceField(
                                        choices = teams,
                                        widget  = forms.Select(),
                                        help_text = "" )
        self.fields['second_team'] = forms.ChoiceField(
                                        choices = teams,
                                        widget  = forms.Select(),
                                        help_text = "" )
        self.fields['third_team'] = forms.ChoiceField(
                                        choices = teams,
                                        widget  = forms.Select(),
                                        help_text = "" )
        self.fields['fourth_team'] = forms.ChoiceField(
                                        choices = teams,
                                        widget  = forms.Select(),
                                        help_text = "" )
        self.fields['fifth_team'] = forms.ChoiceField(
                                        choices = teams,
                                        widget  = forms.Select(),
                                        help_text = "" )
        self.fields['sixth_team'] = forms.ChoiceField(
                                        choices = teams,
                                        widget  = forms.Select(),
                                        help_text = "" )


    class Meta:
        model   = TournamentBet
        exclude = ['player_id', 'tournament_id', 'points_won', 'created_date', 'modified_date']

class BetPointForm( ModelForm ):
    class Meta:
        model   = BetPoint
        fields  = '__all__'