from flask import Blueprint, render_template,request, flash, jsonify
from flask_login import login_required, current_user
from  sqlalchemy.sql.expression import func
from .models import Mythologycard, Note, Geocard, Historycard, Literaturecard, Mathematicscard, Miscellaneouscard, Musicandauditoryartcard,\
    Peoplecard, Performancecard, Philosophycard, Popularculturecard, Religioncard, Sciencecard, Socialsciencecard, Sportscard, Visualartcard
from . import db
import json

#Defines that this file is a blueprint of my application
views=Blueprint('views', __name__)

#Defines the first route and runs whenever we go to the route
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method=='POST':
        note=request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note=Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
            
    return render_template("home.html", user=current_user)    #reference current user and check if it's authenticated

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note=json.loads(request.data)
    noteId=note['noteId']
    note=Note.query.get(noteId)
    if note:
        if note.user_id==current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/practice', methods=['GET', 'POST'])
@login_required
def practice():
    return render_template("practice.html", user=current_user)

@views.route('/test-yourself', methods=['GET', 'POST'])
@login_required
def test_yourself():
    return render_template("test-yourself.html", user=current_user)

@views.route('/test-yourself/geography')
@login_required
def test_yourself_geography():
    return render_template("test-yourself/geography.html", user=current_user)

@views.route('/test-yourself/history')
@login_required
def test_yourself_history():
    return render_template("test-yourself/history.html", user=current_user)

@views.route('/test-yourself/literature')
@login_required
def test_yourself_literature():
    return render_template("test-yourself/literature.html", user=current_user)

@views.route('/test-yourself/mathematics')
@login_required
def test_yourself_mathematics():
    return render_template("test-yourself/mathematics.html", user=current_user)

@views.route('/test-yourself/miscellaneous')
@login_required
def test_yourself_miscellaneous():
    return render_template("test-yourself/miscellaneous.html", user=current_user)

@views.route('/test-yourself/music-and-auditory-art')
@login_required
def test_yourself_music_and_auditory_art():
    return render_template("test-yourself/music-and-auditory-art.html", user=current_user)

@views.route('/test-yourself/mythology')
@login_required
def test_yourself_mythology():
    return render_template("test-yourself/mythology.html", user=current_user)

@views.route('/test-yourself/people')
@login_required
def test_yourself_people():
    return render_template("test-yourself/people.html", user=current_user)

@views.route('/test-yourself/performance')
@login_required
def test_yourself_performance():
    return render_template("test-yourself/performance.html", user=current_user)

@views.route('/test-yourself/philosophy')
@login_required
def test_yourself_philosophy():
    return render_template("test-yourself/philosophy.html", user=current_user)

@views.route('/test-yourself/popular-culture')
@login_required
def test_yourselfpopular_culture():
    return render_template("test-yourself/popular-culture.html", user=current_user)

@views.route('/test-yourself/religion')
@login_required
def test_yourselfreligion():
    return render_template("test-yourself/religion.html", user=current_user)

@views.route('/test-yourself/science')
@login_required
def test_yourself_science():
    return render_template("test-yourself/science.html", user=current_user)

@views.route('/test-yourself/social-science')
@login_required
def test_yourself_social_science():
    return render_template("test-yourself/social-science.html", user=current_user)

@views.route('/test-yourself/sports')
@login_required
def test_yourself_sports():
    return render_template("test-yourself/sports.html", user=current_user)

@views.route('/test-yourself/visual-art')
@login_required
def test_yourself_visual_art():
    return render_template("test-yourself/visual-art.html", user=current_user)

@views.route('/test-yourself/tournament-simulator')
@login_required
def test_yourself_tournament_simulator():
    return render_template("test-yourself/tournament-simulator.html", user=current_user)

@views.route('/practice/you-gotta-know/geography')
@login_required
def you_gotta_know_geography():
    return render_template("practice/you-gotta-know/geography.html", user=current_user)

@views.route('/practice/you-gotta-know/geography/active-volcanoes')
@login_required
def you_gotta_know_geography_active_volcanoes():
    return render_template("/practice/you-gotta-know/geography/active-volcanoes.html", user=current_user)

@views.route('/practice/you-gotta-know/geography/african-bodies-of-water')
@login_required
def you_gotta_know_geography_african_bodies_of_water():
    return render_template("/practice/you-gotta-know/geography/african-bodies-of-water.html", user=current_user)

@views.route('/practice/you-gotta-know/geography/asian-rivers')
@login_required
def you_gotta_know_geography__asian_rivers():
    return render_template("practice/you-gotta-know/geography/african-bodies-of-water.html", user=current_user)

@views.route('/practice/you-gotta-know/geography/deserts')
@login_required
def you_gotta_know_geography__deserts():
    return render_template("practice/you-gotta-know/geography/deserts.html", user=current_user)

@views.route('/practice/you-gotta-know/geography/mountains')
@login_required
def you_gotta_know_geography__mountains():
    return render_template("practice/you-gotta-know/geography/mountains.html", user=current_user)

@views.route('/practice/you-gotta-know/geography/north-american-rivers')
@login_required
def you_gotta_know_geography__north_american_rivers():
    return render_template("practice/you-gotta-know/geography/north-american-rivers.html", user=current_user)

@views.route('/practice/you-gotta-know/geography/western-european-rivers')
@login_required
def you_gotta_know_geography__western_eurpean_rivers():
    return render_template("practice/you-gotta-know/geography/western-european-rivers.html", user=current_user)

@views.route('/practice/you-gotta-know/history')
@login_required
def you_gotta_know_history():
    return render_template("practice/you-gotta-know/history.html", user=current_user)

@views.route('/practice/you-gotta-know/history/20th-century-african-leaders')
@login_required
def you_gotta_know_history_20th_century_african_leaders():
    return render_template("/practice/you-gotta-know/history/20th-century-african-leaders.html", user=current_user)

@views.route('/practice/you-gotta-know/history/20th-century-middle-eastern-leaders')
@login_required
def you_gotta_know_history_history_20th_century_middle_eastern_leaders():
    return render_template("practice/you-gotta-know/history/20th-century-middle-eastern-leaders.html", user=current_user)

@views.route('/practice/you-gotta-know/history/african-american-civil-rights-leaders')
@login_required
def you_gotta_know_history_20th_african_american_civil_rights_leaders():
    return render_template("practice/you-gotta-know/history/african-american-civil-rights-leaders.html", user=current_user)

@views.route('/practice/you-gotta-know/history/american-murders-and-muderers')
@login_required
def you_gotta_know_history_20th_american_murders_and_murderers():
    return render_template("practice/you-gotta-know/history/american-murders-and-murderers.html", user=current_user)

@views.route('/practice/you-gotta-know/history/american-third-parties')
@login_required
def you_gotta_know_history_20th_american_third_parties():
    return render_template("practice/you-gotta-know/history/american-third-parties.html", user=current_user)

@views.route('/practice/you-gotta-know/history/american-warships')
@login_required
def you_gotta_know_history_20th_american_warships():
    return render_template("practice/you-gotta-know/history/american-warships.html", user=current_user)

@views.route('/practice/you-gotta-know/history/ancient-empires-of-the-mediterranean-and-near-east')
@login_required
def you_gotta_know_history_20th_ancient_empires_of_the_mediterranean_and_near_east():
    return render_template("practice/you-gotta-know/history/ancient-empires-of-the-mediterranean-and-near-east.html", user=current_user)

@views.route('/practice/you-gotta-know/history/ancient-greek-places')
@login_required
def you_gotta_know_history_20th_ancient_greek_places():
    return render_template("practice/you-gotta-know/history/ancient-greek-places.html", user=current_user)

@views.route('/practice/you-gotta-know/history/assassinations')
@login_required
def you_gotta_know_history_20th_assassinations():
    return render_template("practice/you-gotta-know/history/assassinations.html", user=current_user)

@views.route('/practice/you-gotta-know/history/aviators')
@login_required
def you_gotta_know_history_20th_aviators():
    return render_template("practice/you-gotta-know/history/aviators.html", user=current_user)

@views.route('/practice/you-gotta-know/history/battles-of-the-ancient-world')
@login_required
def you_gotta_know_history_20th_battles_of_the_ancient_world():
    return render_template("practice/you-gotta-know/history/battles-of-the-ancient-world.html", user=current_user)

@views.route('/practice/you-gotta-know/history/black-american-legislators')
@login_required
def you_gotta_know_history_20th_black_american_legislators():
    return render_template("practice/you-gotta-know/history/black-american-legislators.html", user=current_user)

@views.route('/practice/you-gotta-know/history/british-monarchs')
@login_required
def you_gotta_know_history_20th_british_monarchs():
    return render_template("practice/you-gotta-know/history/british-monarchs.html", user=current_user)

@views.route('/practice/you-gotta-know/history/british-prime-ministers')
@login_required
def you_gotta_know_history_20th_british_prime_ministers():
    return render_template("practice/you-gotta-know/history/british-prime-ministers.html", user=current_user)

@views.route('/practice/you-gotta-know/history/british-reform-movements')
@login_required
def you_gotta_know_history_20th_british_reform_movements():
    return render_template("practice/you-gotta-know/history/british-reform-movements.html", user=current_user)

@views.route('/practice/you-gotta-know/history/campaigns-in-the-pacific-theater-of-world-war-2')
@login_required
def you_gotta_know_history_20th_campaigns_in_the_pacific_theater_of_world_war_2():
    return render_template("practice/you-gotta-know/history/campaigns-in-the-pacific-theater-of-world-war-2.html", user=current_user)

@views.route('/practice/you-gotta-know/history/chinese-dynasties')
@login_required
def you_gotta_know_history_20th_chinese_dynasties():
    return render_template("practice/you-gotta-know/history/chinese-dynasties.html", user=current_user)

@views.route('/practice/you-gotta-know/history/civil-war-battles')
@login_required
def you_gotta_know_history_20th_civil_war_battles():
    return render_template("practice/you-gotta-know/history/civil-war-battles.html", user=current_user)

@views.route('/practice/you-gotta-know/history/countries-once-known-by-different-names')
@login_required
def you_gotta_know_history_20th_countries_once_known_by_different_names():
    return render_template("practice/you-gotta-know/history/countries-once-known-by-different-names.html", user=current_user)

@views.route('/practice/you-gotta-know/history/elections')
@login_required
def you_gotta_know_history_20th_elections():
    return render_template("practice/you-gotta-know/history/elections.html", user=current_user)

@views.route('/practice/you-gotta-know/history/european-royal-families')
@login_required
def you_gotta_know_history_20th_european_royal_families():
    return render_template("practice/you-gotta-know/history/european-royal-families.html", user=current_user)

@views.route('/practice/you-gotta-know/history/explorers')
@login_required
def you_gotta_know_history_20th_explorers():
    return render_template("practice/you-gotta-know/history/explorers.html", user=current_user)

@views.route('/practice/you-gotta-know/history/feminists')
@login_required
def you_gotta_know_history_20th_feminists():
    return render_template("practice/you-gotta-know/history/feminists.html", user=current_user)

@views.route('/practice/you-gotta-know/history/founders-of-religious-traditions')
@login_required
def you_gotta_know_history_20th_founders_of_religious_traditions():
    return render_template("practice/you-gotta-know/history/founders-of-religious-traditions.html", user=current_user)

@views.route('/practice/you-gotta-know/history/kings-of-france')
@login_required
def you_gotta_know_history_20th_kings_of_france():
    return render_template("practice/you-gotta-know/history/kings-of-france.html", user=current_user)

@views.route('/practice/you-gotta-know/history/magazines-from-american-history')
@login_required
def you_gotta_know_history_20th_magazines_from_american_history():
    return render_template("practice/you-gotta-know/history/magazines-from-american-history.html", user=current_user)

@views.route('/practice/you-gotta-know/history/massacres')
@login_required
def you_gotta_know_history_20th_massacres():
    return render_template("practice/you-gotta-know/history/massacres.html", user=current_user)

@views.route('/practice/you-gotta-know/history/medieval-battles')
@login_required
def you_gotta_know_history_20th_medieval_battles():
    return render_template("practice/you-gotta-know/history/medieval-battles.html", user=current_user)

@views.route('/practice/you-gotta-know/history/medieval-islamic-dynasties')
@login_required
def you_gotta_know_history_20th_medieval_islamic_dynasties():
    return render_template("practice/you-gotta-know/history/medieval-islamic-dynasties.html", user=current_user)

@views.route('/practice/you-gotta-know/history/mexican-leaders')
@login_required
def you_gotta_know_history_20th_mexican_leaders():
    return render_template("practice/you-gotta-know/history/mexican-leaders.html", user=current_user)

@views.route('/practice/you-gotta-know/history/modern-speeches')
@login_required
def you_gotta_know_history_20th_modern_speeches():
    return render_template("practice/you-gotta-know/history/modern-speeches.html", user=current_user)

@views.route('/practice/you-gotta-know/history/napoleonic-battles')
@login_required
def you_gotta_know_history_20th_napoleonic_battles():
    return render_template("practice/you-gotta-know/history/napoleonic-battles.html", user=current_user)

@views.route('/practice/you-gotta-know/history/native-american-people')
@login_required
def you_gotta_know_history_20th_native_american_people():
    return render_template("practice/you-gotta-know/history/native-american-people.html", user=current_user)

@views.route('/practice/you-gotta-know/history/people-of-the-early-middle-ages')
@login_required
def people_of_the_early_middle_ages():
    return render_template("practice/you-gotta-know/history/people-of-the-early-middle-ages.html", user=current_user)

@views.route('/practice/you-gotta-know/history/popes')
@login_required
def you_gotta_know_history_20th_popes():
    return render_template("practice/you-gotta-know/history/popes.html", user=current_user)

@views.route('/practice/you-gotta-know/history/presidential-inaugurations')
@login_required
def you_gotta_know_history_20th_presidential_inaugurations():
    return render_template("practice/you-gotta-know/history/presidential-inaugurations.html", user=current_user)

@views.route('/practice/you-gotta-know/history/revolutionary-war-battles')
@login_required
def you_gotta_know_history_20th_revolutionary_war_battles():
    return render_template("practice/you-gotta-know/history/revolutionary-war-battles.html", user=current_user)

@views.route('/practice/you-gotta-know/history/revolutionary-war-generals')
@login_required
def you_gotta_know_history_20th_revolutionary_war_generals():
    return render_template("practice/you-gotta-know/history/revolutionary-war-generals.html", user=current_user)

@views.route('/practice/you-gotta-know/history/roman-emperors')
@login_required
def you_gotta_know_history_20th_roman_emperors():
    return render_template("practice/you-gotta-know/history/roman-emperors.html", user=current_user)

@views.route('/practice/you-gotta-know/history/russian-tsars')
@login_required
def you_gotta_know_history_20th_russian_tsars():
    return render_template("practice/you-gotta-know/history/russian-tsars.html", user=current_user)

@views.route('/practice/you-gotta-know/history/secretaries-of-state')
@login_required
def you_gotta_know_history_20th_secretaries_of_state():
    return render_template("practice/you-gotta-know/history/secretaries-of-state.html", user=current_user)

@views.route('/practice/you-gotta-know/history/south-american-political-leaders')
@login_required
def you_gotta_know_history_20th_south_american_political_leaders():
    return render_template("practice/you-gotta-know/history/south-american-political-leaders.html", user=current_user)

@views.route('/practice/you-gotta-know/history/space-missions')
@login_required
def you_gotta_know_history_20th_space_missions():
    return render_template("practice/you-gotta-know/history/space-missions.html", user=current_user)

@views.route('/practice/you-gotta-know/history/spies')
@login_required
def you_gotta_know_history_20th_spies():
    return render_template("practice/you-gotta-know/history/spies.html", user=current_user)

@views.route('/practice/you-gotta-know/history/supreme-court-cases-part-1')
@login_required
def you_gotta_know_history_20th_supreme_court_cases_part_1():
    return render_template("practice/you-gotta-know/history/supreme-court-cases-part-1.html", user=current_user)

@views.route('/practice/you-gotta-know/history/supreme-court-cases-part-2')
@login_required
def you_gotta_know_history_20th_supreme_court_cases_part_2():
    return render_template("practice/you-gotta-know/history/supreme-court-cases-part-2.html", user=current_user)

@views.route('/practice/you-gotta-know/history/supreme-court-cases-concerned-with-african-americans')
@login_required
def you_gotta_know_history_20th_supreme_court_cases_concerned_with_african_americans():
    return render_template("practice/you-gotta-know/history/supreme-court-cases-concerned-with-african-americans.html", user=current_user)

@views.route('/practice/you-gotta-know/history/treaties')
@login_required
def you_gotta_know_history_20th_treaties():
    return render_template("practice/you-gotta-know/history/treaties.html", user=current_user)

@views.route('/practice/you-gotta-know/history/world-war-2-battles')
@login_required
def you_gotta_know_history20th_world_war_2_battles():
    return render_template("practice/you-gotta-know/history/world-war-2-battles.html", user=current_user)

@views.route('/practice/you-gotta-know/literature')
@login_required
def you_gotta_know_literature():
    return render_template("practice/you-gotta-know/literature.html", user=current_user)

@views.route('/practice/you-gotta-know/literature/african-american-authors')
@login_required
def you_gotta_know_literature_african_american_authors():
    return render_template("practice/you-gotta-know/literature/african-american-authors.html", user=current_user)

@views.route('/practice/you-gotta-know/literature/american-plays')
@login_required
def you_gotta_know_literature_american_plays():
    return render_template("practice/you-gotta-know/literature/american-plays.html", user=current_user)

@views.route('/practice/you-gotta-know/literature/ancient-greek-plays')
@login_required
def you_gotta_know_literature_ancient_greek_plays():
    return render_template("practice/you-gotta-know/literature/ancient-greek-plays.html", user=current_user)

@views.route('/practice/you-gotta-know/literature/authors-of-speculative-fiction')
@login_required
def you_gotta_know_literature_authors_of_speculative_fiction():
    return render_template("practice/you-gotta-know/literature/authors-of-speculative-fiction.html", user=current_user)

@views.route('/practice/you-gotta-know/literature/characters-in-the-hebrew-bible')
@login_required
def you_gotta_know_literature_characters_in_the_hebrew_bible():
    return render_template("practice/you-gotta-know/literature/characters-in-the-hebrew-bible.html", user=current_user)

@views.route('/practice/you-gotta-know/literature/charles-dickens-novels')
@login_required
def you_gotta_know_literature_charles_dickens_novels():
    return render_template("practice/you-gotta-know/literature/charles-dickens-novels.html", user=current_user)

@views.route('/practice/you-gotta-know/literature/japanese-authors')
@login_required
def you_gotta_know_literature_japanese_authors():
    return render_template("practice/you-gotta-know/literature/japanese-authors.html", user=current_user)

@views.route('/practice/you-gotta-know/literature/latin-american-authors')
@login_required
def you_gotta_know_literature_latin_american_authors():
    return render_template("practice/you-gotta-know/literature/latin-american-authors.html", user=current_user)

@views.route('/practice/you-gotta-know/literature/non-shakespeare-classical-english-dramas')
@login_required
def you_gotta_know_literature_non_shakespeare_classical_english_dramas():
    return render_template("practice/you-gotta-know/literature/non-shakespeare-classical-english-dramas.html", user=current_user)

@views.route('/practice/you-gotta-know/literature/postmodern-authors')
@login_required
def you_gotta_know_literature_postmodern_authors():
    return render_template("practice/you-gotta-know/literature/postmodern-authors.html", user=current_user)

@views.route('/practice/you-gotta-know/literature/religious-texts')
@login_required
def you_gotta_know_literature_religious_texts():
    return render_template("practice/you-gotta-know/literature/religious-texts.html", user=current_user)

@views.route('/practice/you-gotta-know/literature/shakespearean-speeches-monologues-and-soliloquies')
@login_required
def you_gotta_know_literature_shakespearean_speeches_monologues_and_soliloquies():
    return render_template("practice/you-gotta-know/literature/shakespearean-speeches-monologues-and-soliloquies.html", user=current_user)

@views.route('/practice/you-gotta-know/literature/shakespearean-villains')
@login_required
def you_gotta_know_literature_shakespearean_villains():
    return render_template("practice/you-gotta-know/literature/shakespearean-villains.html", user=current_user)

@views.route('/practice/you-gotta-know/literature/short-story-authors')
@login_required
def you_gotta_know_literature_short_story_authors():
    return render_template("practice/you-gotta-know/literature/short-story-authors.html", user=current_user)

@views.route('/practice/you-gotta-know/literature/translations-and-translators')
@login_required
def you_gotta_know_literature_translations_and_translators():
    return render_template("practice/you-gotta-know/literature/translations-and-translators.html", user=current_user)

@views.route('/practice/you-gotta-know/literature/works-of-mystery-and-detective-fiction')
@login_required
def you_gotta_know_literature_works_of_mystery_and_detective_fiction():
    return render_template("practice/you-gotta-know/literature/works-of-mystery-and-detective-fiction.html", user=current_user)

@views.route('/practice/you-gotta-know/literature/works-of-russian-short-fiction')
@login_required
def you_gotta_know_literature_works_of_russian_short_fiction():
    return render_template("practice/you-gotta-know/literature/works-of-russian-short-fiction.html", user=current_user)

@views.route('/practice/you-gotta-know/mathematics')
@login_required
def you_gotta_know_mathematics():
    return render_template("practice/you-gotta-know/mathematics.html", user=current_user) 

@views.route('/practice/you-gotta-know/mathematics/classifications-of-mathematical-functions')
@login_required
def you_gotta_know_mathematics_classifications_of_mathematical_functions():
    return render_template("practice/you-gotta-know/mathematics/classifications-of-mathematical-functions.html", user=current_user) 

@views.route('/practice/you-gotta-know/mathematics/mathematicians')
@login_required
def you_gotta_know_mathematics_mathematicians():
    return render_template("practice/you-gotta-know/mathematics/mathematicians.html", user=current_user) 

@views.route('/practice/you-gotta-know/mathematics/types-of-computation-problems')
@login_required
def you_gotta_know_mathematics_types_of_computation_problems():
    return render_template("practice/you-gotta-know/mathematics/types-of-computation-problems.html", user=current_user) 

@views.route('/practice/you-gotta-know/miscellaneous')
@login_required
def you_gotta_know_miscellaneous():
    return render_template("practice/you-gotta-know/miscellaneous.html", user=current_user) 

@views.route('/practice/you-gotta-know/miscellaneous/common-mistakes-part-1')
@login_required
def you_gotta_know_miscellaneous_common_mistakes_part_1():
    return render_template("practice/you-gotta-know/miscellaneous/common-mistakes-part-1.html", user=current_user)

@views.route('/practice/you-gotta-know/miscellaneous/common-mistakes-part-2')
@login_required
def you_gotta_know_miscellaneous_common_mistakes_part_2():
    return render_template("practice/you-gotta-know/miscellaneous/common-mistakes-part-2.html", user=current_user) 

@views.route('/practice/you-gotta-know/miscellaneous/quintuples')
@login_required
def you_gotta_know_miscellaneous_quintuples():
    return render_template("practice/you-gotta-know/miscellaneous/quintuples.html", user=current_user)

@views.route('/practice/you-gotta-know/music-and-auditory-art')
@login_required
def you_gotta_know_music_and_auditory_art():
    return render_template("/practice/you-gotta-know/music-and-auditory-art.html", user=current_user)

@views.route('/practice/you-gotta-know/music-and-auditory-art/20th-century-composers')
@login_required
def you_gotta_know_music_and_auditory_art_20th_century_composers():
    return render_template("/practice/you-gotta-know/music-and-auditory-art/20th-century-composers.html", user=current_user) 

@views.route('/practice/you-gotta-know/music-and-auditory-art/american-composers')
@login_required
def you_gotta_know_music_and_auditory_art_american_composers():
    return render_template("/practice/you-gotta-know/music-and-auditory-art/american-composers.html", user=current_user) 

@views.route('/practice/you-gotta-know/music-and-auditory-art/music-theory-terms')
@login_required
def you_gotta_know_music_and_auditory_art_music_theory_terms():
    return render_template("/practice/you-gotta-know/music-and-auditory-art/music-theory-terms.html", user=current_user) 

@views.route('/practice/you-gotta-know/music-and-auditory-art/musicals-part-1')
@login_required
def you_gotta_know_music_and_auditory_art_musicals_part_1():
    return render_template("/practice/you-gotta-know/music-and-auditory-art/musicals-part-1.html", user=current_user) 

@views.route('/practice/you-gotta-know/music-and-auditory-art/musicals-part-2')
@login_required
def you_gotta_know_music_and_auditory_art_musicals_part_2():
    return render_template("/practice/you-gotta-know/music-and-auditory-art/musicals-part-2.html", user=current_user) 

@views.route('/practice/you-gotta-know/music-and-auditory-art/operas')
@login_required
def you_gotta_know_music_and_auditory_art_operas():
    return render_template("/practice/you-gotta-know/music-and-auditory-art/operas.html", user=current_user) 

@views.route('/practice/you-gotta-know/music-and-auditory-art/romantic-era-composers')
@login_required
def you_gotta_know_music_and_auditory_art_romantic_era_composers():
    return render_template("/practice/you-gotta-know/music-and-auditory-art/romantic-era-composers.html", user=current_user) 

@views.route('/practice/you-gotta-know/music-and-auditory-art/works-by-ludwig-van-beethoven')
@login_required
def you_gotta_know_music_and_auditory_art_works_by_ludwig_van_beethoven():
    return render_template("/practice/you-gotta-know/music-and-auditory-art/works-by-ludwig-van-beethoven.html", user=current_user) 

@views.route('/practice/you-gotta-know/music-and-auditory-art/works-by-mozart')
@login_required
def you_gotta_know_music_and_auditory_art_works_by_mozart():
    return render_template("/practice/you-gotta-know/music-and-auditory-art/works-by-mozart.html", user=current_user)

@views.route('/practice/you-gotta-know/mythology')
@login_required
def you_gotta_know_mythology():
    return render_template("practice/you-gotta-know/mythology.html", user=current_user)  

@views.route('/practice/you-gotta-know/mythology/arthurian-characters')
@login_required
def you_gotta_know_mythology_arthurian_characters():
    return render_template("practice/you-gotta-know/mythology/arthurian-characters.html", user=current_user) 

@views.route('/practice/you-gotta-know/mythology/egyptian-deities')
@login_required
def you_gotta_know_mythology_egyptian_deities():
    return render_template("practice/you-gotta-know/mythology/egyptian-deities.html", user=current_user) 

@views.route('/practice/you-gotta-know/mythology/greek-heroes')
@login_required
def you_gotta_know_mythology_greek_heroes():
    return render_template("practice/you-gotta-know/mythology/greek-heroes.html", user=current_user)

@views.route('/practice/you-gotta-know/mythology/greek-mythological-monsters')
@login_required
def you_gotta_know_mythology_greek_mythological_monsters():
    return render_template("practice/you-gotta-know/mythology/greek-mythological-monsters.html", user=current_user) 

@views.route('/practice/you-gotta-know/mythology/mortal-women-in-greek-myth')
@login_required
def you_gotta_know_mythology_mortal_women_in_greek_myth():
    return render_template("practice/you-gotta-know/mythology/mortal-women-in-greek-myth.html", user=current_user) 

@views.route('/practice/you-gotta-know/mythology/norse-gods')
@login_required
def you_gotta_know_mythology_norse_gods():
    return render_template("practice/you-gotta-know/mythology/norse-gods.html", user=current_user) 

@views.route('/practice/you-gotta-know/mythology/trojan-war-heroes')
@login_required
def you_gotta_know_mythology_trojan_war_heroes():
    return render_template("practice/you-gotta-know/mythology/trojan-war-heroes.html", user=current_user)

@views.route('/practice/you-gotta-know/people')
@login_required
def you_gotta_know_people():
    return render_template("practice/you-gotta-know/people.html", user=current_user)

@views.route('/practice/you-gotta-know/people/20th-century-african-leaders')
@login_required
def you_gotta_know_people__20th_century_african_leaders():
    return render_template("practice/you-gotta-know/people/20th-century-african-leaders.html", user=current_user)

@views.route('/practice/you-gotta-know/people/20th-century-composers')
@login_required
def you_gotta_know_people__20th_century_composers():
    return render_template("practice/you-gotta-know/people/20th-century-composers.html", user=current_user)

@views.route('/practice/you-gotta-know/people/20th-century-middle-eastern-leaders')
@login_required
def you_gotta_know_people__people_20th_century_middle_eastern_leaders():
    return render_template("practice/you-gotta-know/people/20th-century-middle-eastern-leaders.html", user=current_user)

@views.route('/practice/you-gotta-know/people/african-american-authors')
@login_required
def you_gotta_know_people__people_african_american_authors():
    return render_template("practice/you-gotta-know/people/african-american-authors.html", user=current_user)

@views.route('/practice/you-gotta-know/people/african-american-civil-rights-leaders')
@login_required
def you_gotta_know_people_african_american_civil_rights_leaders():
    return render_template("practice/you-gotta-know/people/african-american-civil-rights-leaders.html", user=current_user)

@views.route('/practice/you-gotta-know/people/american-composers')
@login_required
def you_gotta_know_people_american_composers():
    return render_template("practice/you-gotta-know/people/american-composers.html", user=current_user)

@views.route('/practice/you-gotta-know/people/ancient-philosophers')
@login_required
def you_gotta_know_people_ancient_philosophers():
    return render_template("practice/you-gotta-know/people/ancient-philosophers.html", user=current_user)

@views.route('/practice/you-gotta-know/people/anthropologists')
@login_required
def you_gotta_know_people_anthropologists():
    return render_template("practice/you-gotta-know/people/anthropologists.html", user=current_user)

@views.route('/practice/you-gotta-know/people/architects')
@login_required
def you_gotta_know_people_architects():
    return render_template("practice/you-gotta-know/people/architects.html", user=current_user)

@views.route('/practice/you-gotta-know/people/assassinations')
@login_required
def you_gotta_know_people_assassinations():
    return render_template("practice/you-gotta-know/people/assassinations.html", user=current_user)

@views.route('/practice/you-gotta-know/people/authors-of-speculative-fiction')
@login_required
def you_gotta_know_people_authors_of_speculative_fiction():
    return render_template("practice/you-gotta-know/people/authors-of-speculative-fiction.html", user=current_user)

@views.route('/practice/you-gotta-know/people/aviators')
@login_required
def you_gotta_know_people_aviators():
    return render_template("practice/you-gotta-know/people/aviators.html", user=current_user)

@views.route('/practice/you-gotta-know/people/black-american-legislators')
@login_required
def you_gotta_know_people_black_american_legislators():
    return render_template("practice/you-gotta-know/people/black-american-legislators.html", user=current_user)

@views.route('/practice/you-gotta-know/people/british-prime-ministers')
@login_required
def you_gotta_know_people_british_prime_ministers():
    return render_template("practice/you-gotta-know/people/british-prime-ministers.html", user=current_user)

@views.route('/practice/you-gotta-know/people/choreographers')
@login_required
def you_gotta_know_people_choreographers():
    return render_template("practice/you-gotta-know/people/choreographers.html", user=current_user)

@views.route('/practice/you-gotta-know/people/economists')
@login_required
def you_gotta_know_people_economists():
    return render_template("practice/you-gotta-know/people/economists.html", user=current_user)

@views.route('/practice/you-gotta-know/people/explorers')
@login_required
def you_gotta_know_people_explorers():
    return render_template("practice/you-gotta-know/people/explorers.html", user=current_user)

@views.route('/practice/you-gotta-know/people/feminists')
@login_required
def you_gotta_know_people_feminists():
    return render_template("practice/you-gotta-know/people/feminists.html", user=current_user)

@views.route('/practice/you-gotta-know/people/founders-of-religious-traditions')
@login_required
def you_gotta_know_people_founders_of_religious_traditions():
    return render_template("practice/you-gotta-know/people/founders-of-religious-traditions.html", user=current_user)

@views.route('/practice/you-gotta-know/people/golfers')
@login_required
def you_gotta_know_people_golfers():
    return render_template("practice/you-gotta-know/people/golfers.html", user=current_user)

@views.route('/practice/you-gotta-know/people/hockey-hall-of-famers')
@login_required
def you_gotta_know_people_hockey_hall_of_famers():
    return render_template("practice/you-gotta-know/people/hockey-hall-of-famers.html", user=current_user)

@views.route('/practice/you-gotta-know/people/japanese-authors')
@login_required
def you_gotta_know_people_japanese_authors():
    return render_template("practice/you-gotta-know/people/japanese-authors.html", user=current_user)

@views.route('/practice/you-gotta-know/people/kings-of-france')
@login_required
def you_gotta_know_people_kings_of_france():
    return render_template("practice/you-gotta-know/people/kings-of-france.html", user=current_user)

@views.route('/practice/you-gotta-know/people/latin-american-authors')
@login_required
def you_gotta_know_people_latin_american_authors():
    return render_template("practice/you-gotta-know/people/latin-american-authors.html", user=current_user)

@views.route('/practice/you-gotta-know/people/mathematicians')
@login_required
def you_gotta_know_people_mathematicians():
    return render_template("practice/you-gotta-know/people/mathematicians.html", user=current_user)

@views.route('/practice/you-gotta-know/people/mexican-leaders')
@login_required
def you_gotta_know_people_mexican_leaders():
    return render_template("practice/you-gotta-know/people/mexican-leaders.html", user=current_user)

@views.route('/practice/you-gotta-know/people/new-york-yankees')
@login_required
def you_gotta_know_people_new_york_yankees():
    return render_template("practice/you-gotta-know/people/new-york-yankees.html", user=current_user)

@views.route('/practice/you-gotta-know/people/nobel-prize-winners-in-physiology-or-medicine')
@login_required
def you_gotta_know_people_nobel_prize_winners_in_physiology_or_medicine():
    return render_template("practice/you-gotta-know/people/nobel-prize-winners-in-physiology-or-medicine.html", user=current_user)

@views.route('/practice/you-gotta-know/people/photography-pioneers')
@login_required
def you_gotta_know_people_photography_pioneers():
    return render_template("practice/you-gotta-know/people/photography-pioneers.html", user=current_user)

@views.route('/practice/you-gotta-know/people/popes')
@login_required
def you_gotta_know_people_popes():
    return render_template("practice/you-gotta-know/people/popes.html", user=current_user)

@views.route('/practice/you-gotta-know/people/postmodern-authors')
@login_required
def you_gotta_know_people_postmodern_authors():
    return render_template("practice/you-gotta-know/people/postmodern-authors.html", user=current_user)

@views.route('/practice/you-gotta-know/people/psychologists')
@login_required
def you_gotta_know_people_psychologists():
    return render_template("practice/you-gotta-know/people/psychologists.html", user=current_user)

@views.route('/practice/you-gotta-know/people/revolutionary-war-generals')
@login_required
def you_gotta_know_people_revolutionary_war_generals():
    return render_template("practice/you-gotta-know/people/revolutionary-war-generals.html", user=current_user)

@views.route('/practice/you-gotta-know/people/rocket-scientists')
@login_required
def you_gotta_know_people_rocket_scientists():
    return render_template("practice/you-gotta-know/people/rocket-scientists.html", user=current_user)

@views.route('/practice/you-gotta-know/people/roman-emperors')
@login_required
def you_gotta_know_people_roman_emperors():
    return render_template("practice/you-gotta-know/people/roman-emperors.html", user=current_user)

@views.route('/practice/you-gotta-know/people/romatic-era-composers')
@login_required
def you_gotta_know_people_romatic_era_composers():
    return render_template("practice/you-gotta-know/people/romatic-era-composers.html", user=current_user)

@views.route('/practice/you-gotta-know/people/russian-tsars')
@login_required
def you_gotta_know_people_russian_tsars():
    return render_template("practice/you-gotta-know/people/russian-tsars.html", user=current_user)

@views.route('/practice/you-gotta-know/people/sculptors')
@login_required
def you_gotta_know_people_sculptors():
    return render_template("practice/you-gotta-know/people/sculptors.html", user=current_user)

@views.route('/practice/you-gotta-know/people/secretaries-of-state')
@login_required
def you_gotta_know_people_secretaries_of_state():
    return render_template("practice/you-gotta-know/people/secretaries-of-state.html", user=current_user)

@views.route('/practice/you-gotta-know/people/short-story-authors')
@login_required
def you_gotta_know_people_short_story_authors():
    return render_template("practice/you-gotta-know/people/short-story-authors.html", user=current_user)

@views.route('/practice/you-gotta-know/people/south-american-political-leaders')
@login_required
def you_gotta_know_people_south_american_political_leaders():
    return render_template("practice/you-gotta-know/people/south-american-political-leaders.html", user=current_user)

@views.route('/practice/you-gotta-know/people/tennis-players')
@login_required
def you_gotta_know_people_tennis_players():
    return render_template("practice/you-gotta-know/people/tennis-players.html", user=current_user)

@views.route('/practice/you-gotta-know/performance')
@login_required
def you_gotta_know_performance():
    return render_template("practice/you-gotta-know/performance.html", user=current_user)

@views.route('/practice/you-gotta-know/performance/ballets-part-1')
@login_required
def you_gotta_know_performance_ballets_part_1():
    return render_template("practice/you-gotta-know/performance/ballets-part-1.html", user=current_user)

@views.route('/practice/you-gotta-know/performance/ballets-part-2')
@login_required
def you_gotta_know_performance_ballets_part_2():
    return render_template("practice/you-gotta-know/performance/ballets-part-2.html", user=current_user)

@views.route('/practice/you-gotta-know/performance/choreographers')
@login_required
def you_gotta_know_performance_choreographers():
    return render_template("practice/you-gotta-know/performance/choreographers.html", user=current_user)

@views.route('/practice/you-gotta-know/performance/musicals-part-1')
@login_required
def you_gotta_know_performance_musicals_part_1():
    return render_template("practice/you-gotta-know/performance/musicals-part-1.html", user=current_user)

@views.route('/practice/you-gotta-know/performance/musicals-part-2')
@login_required
def you_gotta_know_performance_musicals_part_2():
    return render_template("practice/you-gotta-know/performance/musicals-part-2.html", user=current_user)

@views.route('/practice/you-gotta-know/performance/operas')
@login_required
def you_gotta_know_performance_operas():
    return render_template("practice/you-gotta-know/performance/operas.html", user=current_user)

@views.route('/practice/you-gotta-know/philosophy')
@login_required
def you_gotta_know_performance_philosophy():
    return render_template("practice/you-gotta-know/philosophy.html", user=current_user)

@views.route('/practice/you-gotta-know/philosophy/ancient-philosophers')
@login_required
def you_gotta_know_performance_ancient_philosophers():
    return render_template("practice/you-gotta-know/philosophy/ancient-philosophers.html", user=current_user)

@views.route('/practice/you-gotta-know/philosophy/schools-of-western-philosophy')
@login_required
def you_gotta_know_performance_schools_of_western_philosophy():
    return render_template("practice/you-gotta-know/philosophy/schools-of-western-philosophy.html", user=current_user)

@views.route('/practice/you-gotta-know/popular-culture')
@login_required
def you_gotta_know_popular_culture():
    return render_template("practice/you-gotta-know/popular-culture.html", user=current_user)

@views.route('/practice/you-gotta-know/popular-culture/classic-american-television-series')
@login_required
def you_gotta_know_popular_culture_classic_american_television_series():
    return render_template("practice/you-gotta-know/popular-culture/classic-american-television-series.html", user=current_user)

@views.route('/practice/you-gotta-know/popular-culture/musicals-part-1')
@login_required
def you_gotta_know_popular_culture_musicals_part_1():
    return render_template("practice/you-gotta-know/popular-culture/musicals-part-1.html", user=current_user)

@views.route('/practice/you-gotta-know/popular-culture/musicals-part-2')
@login_required
def you_gotta_know_popular_culture_musicals_part_2():
    return render_template("practice/you-gotta-know/popular-culture/musicals-part-1.html", user=current_user)

@views.route('/practice/you-gotta-know/popular-culture/pre-1960s-movies')
@login_required
def you_gotta_know_popular_culture_pre_1960s_movies():
    return render_template("practice/you-gotta-know/popular-culture/pre-1960s-movies.html", user=current_user)

@views.route('/practice/you-gotta-know/popular-culture/sandbox-and-open-world-video-games')
@login_required
def you_gotta_know_popular_culture_sandbox_and_open_world_video_games():
    return render_template("practice/you-gotta-know/popular-culture/sandbox-and-open-world-video-games.html", user=current_user)

@views.route('/practice/you-gotta-know/popular-culture/video-game-series')
@login_required
def you_gotta_know_popular_culture_video_game_series():
    return render_template("practice/you-gotta-know/popular-culture/video-game-series.html", user=current_user)

@views.route('/practice/you-gotta-know/religion')
@login_required
def you_gotta_know_religion():
    return render_template("practice/you-gotta-know/religion.html", user=current_user)

@views.route('/practice/you-gotta-know/religion/characters-in-the-hebrew-bible')
@login_required
def you_gotta_know_religion_characters_in_the_hebrew_bible():
    return render_template("practice/you-gotta-know/religion/characters-in-the-hebrew-bible.html", user=current_user)

@views.route('/practice/you-gotta-know/religion/founders-of-religious-traditions')
@login_required
def you_gotta_know_religion_founders_of_religious_traditions():
    return render_template("practice/you-gotta-know/religion/founders-of-religious-traditions.html", user=current_user)

@views.route('/practice/you-gotta-know/religion/hindu-gods-and-heroes')
@login_required
def you_gotta_know_religion_hindu_gods_and_heroes():
    return render_template("practice/you-gotta-know/religion/hindu-gods-and-heroes.html", user=current_user)

@views.route('/practice/you-gotta-know/religion/jewish-holidays')
@login_required
def you_gotta_know_religion_jewish_holidays():
    return render_template("practice/you-gotta-know/religion/jewish-holidays.html", user=current_user)

@views.route('/practice/you-gotta-know/religion/jewish-lifecycle-events')
@login_required
def you_gotta_know_religion_jewish_lifecycle_events():
    return render_template("practice/you-gotta-know/religion/jewish-lifecycle-events.html", user=current_user)

@views.route('/practice/you-gotta-know/religion/popes')
@login_required
def you_gotta_know_religion_popes():
    return render_template("practice/you-gotta-know/religion/popes.html", user=current_user)

@views.route('/practice/you-gotta-know/religion/religious-texts')
@login_required
def you_gotta_know_religion_religious_texts():
    return render_template("practice/you-gotta-know/religion/religious-texts.html", user=current_user)

@views.route('/practice/you-gotta-know/science')
@login_required
def you_gotta_know_science():
    return render_template("practice/you-gotta-know/science.html", user=current_user)

@views.route('/practice/you-gotta-know/science/20th-century-physicists')
@login_required
def you_gotta_know_science_20th_century_physicists():
    return render_template("practice/you-gotta-know/science/20th-century-physicists.html", user=current_user)

@views.route('/practice/you-gotta-know/science/active-volcanoes')
@login_required
def you_gotta_know_science_active_volcanoes():
    return render_template("practice/you-gotta-know/science/active-volcanoes.html", user=current_user)

@views.route('/practice/you-gotta-know/science/animal-phyla')
@login_required
def you_gotta_know_science_animal_phyla():
    return render_template("practice/you-gotta-know/science/animal-phyla.html", user=current_user)

@views.route('/practice/you-gotta-know/science/chemical-elements')
@login_required
def you_gotta_know_science_chemical_elements():
    return render_template("practice/you-gotta-know/science/chemical-elements.html", user=current_user)

@views.route('/practice/you-gotta-know/science/chemistry-lab-techniques')
@login_required
def you_gotta_know_science_chemistry_lab_techniques():
    return render_template("practice/you-gotta-know/science/chemistry-lab-techniques.html", user=current_user)

@views.route('/practice/you-gotta-know/science/circuit-components')
@login_required
def you_gotta_know_science_circuit_components():
    return render_template("practice/you-gotta-know/science/circuit-components.html", user=current_user)

@views.route('/practice/you-gotta-know/science/classes-of-particles')
@login_required
def you_gotta_know_science_classes_of_particles():
    return render_template("practice/you-gotta-know/science/classes-of-particles.html", user=current_user)

@views.route('/practice/you-gotta-know/science/classifications-of-mathematical-functions')
@login_required
def you_gotta_know_science_classifications_of_mathematical_functions():
    return render_template("practice/you-gotta-know/science/classifications-of-mathematical-functions.html", user=current_user)

@views.route('/practice/you-gotta-know/science/distinctions-among-types-of-plants')
@login_required
def you_gotta_know_science_distinctions_among_types_of_plants():
    return render_template("practice/you-gotta-know/science/distinctions-among-types-of-plants.html", user=current_user)

@views.route('/practice/you-gotta-know/science/mathematicians')
@login_required
def you_gotta_know_science_mathematicians():
    return render_template("practice/you-gotta-know/science/mathematicians.html", user=current_user)

@views.route('/practice/you-gotta-know/science/moons')
@login_required
def you_gotta_know_science_moons():
    return render_template("practice/you-gotta-know/science/moons.html", user=current_user)

@views.route('/practice/you-gotta-know/science/nobel-prize-winners-in-physiology-or-medicine')
@login_required
def you_gotta_know_science_nobel_prize_winners_in_physiology_or_medicine():
    return render_template("practice/you-gotta-know/science/nobel-prize-winners-in-physiology-or-medicine.html", user=current_user)

@views.route('/practice/you-gotta-know/science/organelles')
@login_required
def _organelles():
    return render_template("practice/you-gotta-know/science/organelles.html", user=current_user)

@views.route('/practice/you-gotta-know/science/programming-terms')
@login_required
def you_gotta_know_science_programming_terms():
    return render_template("practice/you-gotta-know/science/programming-terms.html", user=current_user)

@views.route('/practice/you-gotta-know/science/rocket-scientists')
@login_required
def you_gotta_know_science_rocket_scientists():
    return render_template("practice/you-gotta-know/science/rocket-scientists.html", user=current_user)

@views.route('/practice/you-gotta-know/science/rocks-and-minerals')
@login_required
def you_gotta_know_science_rocks_and_minerals():
    return render_template("practice/you-gotta-know/science/rocks-and-minerals.html", user=current_user)

@views.route('/practice/you-gotta-know/science/scientific-experiments')
@login_required
def you_gotta_know_science_scientific_experiments():
    return render_template("practice/you-gotta-know/science/scientific-experiments.html", user=current_user)

@views.route('/practice/you-gotta-know/science/scientific-scales')
@login_required
def you_gotta_know_science_scientific_scales():
    return render_template("practice/you-gotta-know/science/scientific-scales.html", user=current_user)

@views.route('/practice/you-gotta-know/science/space-missions')
@login_required
def you_gotta_know_science_space_missions():
    return render_template("practice/you-gotta-know/science/space-missions.html", user=current_user)

@views.route('/practice/you-gotta-know/science/types-of-computation-problems')
@login_required
def you_gotta_know_science_types_of_computation_problems():
    return render_template("practice/you-gotta-know/science/types-of-computation-problems.html", user=current_user)

@views.route('/practice/you-gotta-know/social-science')
@login_required
def you_gotta_know_social_science():
    return render_template("practice/you-gotta-know/social-science.html", user=current_user)

@views.route('/practice/you-gotta-know/social-science/anthropologists')
@login_required
def you_gotta_know_social_science_anthropologists():
    return render_template("practice/you-gotta-know/social-science/anthropologists.html", user=current_user)

@views.route('/practice/you-gotta-know/social-science/economic-concepts')
@login_required
def you_gotta_know_social_science_economic_concepts():
    return render_template("practice/you-gotta-know/social-science/economic-concepts.html", user=current_user)

@views.route('/practice/you-gotta-know/social-science/economists')
@login_required
def you_gotta_know_social_science_economists():
    return render_template("practice/you-gotta-know/social-science/economists.html", user=current_user)

@views.route('/practice/you-gotta-know/social-science/psychological-experiments-and-studies')
@login_required
def you_gotta_know_social_science_psychological_experiments_and_studies():
    return render_template("practice/you-gotta-know/social-science/psychological-experiments-and-studies.html", user=current_user)

@views.route('/practice/you-gotta-know/social-science/psychologists')
@login_required
def you_gotta_know_social_science_psychologists():
    return render_template("practice/you-gotta-know/social-science/psychologists.html", user=current_user)

@views.route('/practice/you-gotta-know/sports')
@login_required
def you_gotta_know_sports():
    return render_template("practice/you-gotta-know/sports.html", user=current_user)

@views.route('/practice/you-gotta-know/sports/golfers')
@login_required
def you_gotta_know_sports_golfers():
    return render_template("practice/you-gotta-know/sports/golfers.html", user=current_user)

@views.route('/practice/you-gotta-know/sports/hockey-hall-of-famers')
@login_required
def you_gotta_know_sports_hockey_hall_of_famers():
    return render_template("practice/you-gotta-know/sports/hockey-hall-of-famers.html", user=current_user)

@views.route('/practice/you-gotta-know/sports/new-york-yankees')
@login_required
def you_gotta_know_sports_new_york_yankees():
    return render_template("practice/you-gotta-know/sports/new-york-yankees.html", user=current_user)

@views.route('/practice/you-gotta-know/sports/olympics-pre-2000')
@login_required
def you_gotta_know_sports_olympics_pre_2000():
    return render_template("practice/you-gotta-know/sports/olympics-pre-2000.html", user=current_user)

@views.route('/practice/you-gotta-know/sports/tennis-players')
@login_required
def you_gotta_know_sports_tennis_players():
    return render_template("practice/you-gotta-know/sports/tennis-players.html", user=current_user)

@views.route('/practice/you-gotta-know/visual-art')
@login_required
def you_gotta_know_visual_art():
    return render_template("practice/you-gotta-know/visual-art.html", user=current_user)

@views.route('/practice/you-gotta-know/visual-art/20th-century-paintings')
@login_required
def you_gotta_know_visual_art_20th_century_paintings():
    return render_template("practice/you-gotta-know/visual-art/20th-century-paintings.html", user=current_user)

@views.route('/practice/you-gotta-know/visual-art/architects')
@login_required
def you_gotta_know_visual_art_architects():
    return render_template("practice/you-gotta-know/visual-art/architects.html", user=current_user)

@views.route('/practice/you-gotta-know/visual-art/art-museums')
@login_required
def you_gotta_know_visual_art_art_museums():
    return render_template("practice/you-gotta-know/visual-art/art-museums.html", user=current_user)

@views.route('/practice/you-gotta-know/visual-art/baroque-painters')
@login_required
def you_gotta_know_visual_art_baroque_painters():
    return render_template("practice/you-gotta-know/visual-art/baroque-painters.html", user=current_user)

@views.route('/practice/you-gotta-know/visual-art/dutch-paintings')
@login_required
def you_gotta_know_visual_art_dutch_paintings():
    return render_template("practice/you-gotta-know/visual-art/dutch-paintings.html", user=current_user)

@views.route('/practice/you-gotta-know/visual-art/early-20th-century-art-movements')
@login_required
def you_gotta_know_visual_art_early_20th_century_art_movements():
    return render_template("practice/you-gotta-know/visual-art/early-20th-century-art-movements.html", user=current_user)

@views.route('/practice/you-gotta-know/visual-art/photography-pioneers')
@login_required
def you_gotta_know_visual_art_photography_pioneers():
    return render_template("practice/you-gotta-know/visual-art/photography-pioneers.html", user=current_user)

@views.route('/practice/you-gotta-know/visual-art/sculptors')
@login_required
def you_gotta_know_visual_art_sculptors():
    return render_template("practice/you-gotta-know/visual-art/sculptors.html", user=current_user)

@views.route('/practice/you-gotta-know/visual-art/skyscrapers')
@login_required
def you_gotta_know_visual_art_skyscrapers():
    return render_template("practice/you-gotta-know/visual-art/skyscrapers.html", user=current_user)

@views.route('/practice/flashcards/geography')
@login_required
def flashcards_geography():
    geocard  = Geocard.query.order_by(func.random()).limit(1)
    return render_template("practice/flashcards/geography.html", user=current_user, geocard=geocard)

@views.route('/practice/flashcards/history')
@login_required
def flashcards_history():
    historycard  = Historycard.query.order_by(func.random()).limit(1)
    return render_template("practice/flashcards/history.html", user=current_user, historycard=historycard)

@views.route('/practice/flashcards/literature')
@login_required
def flashcards_literature():
    literaturecard  = Literaturecard.query.order_by(func.random()).limit(1)
    return render_template("practice/flashcards/literature.html", user=current_user, literaturecard=literaturecard)

@views.route('/practice/flashcards/mathematics')
@login_required
def flashcards_mathematics():
    mathematicscard  = Mathematicscard.query.order_by(func.random()).limit(1)
    return render_template("practice/flashcards/mathematics.html", user=current_user, mathematicscard=mathematicscard)

@views.route('/practice/flashcards/miscellaneous')
@login_required
def flashcards_miscellaneous():
    miscellaneouscard  = Miscellaneouscard.query.order_by(func.random()).limit(1)
    return render_template("practice/flashcards/miscellaneous.html", user=current_user, miscellaneouscard=miscellaneouscard)

@views.route('/practice/flashcards/music-and-auditory-art')
@login_required
def flashcards_music_and_auditory_art():
    musicandauditoryartcard  = Musicandauditoryartcard.query.order_by(func.random()).limit(1)
    return render_template("practice/flashcards/music-and-auditory-art.html", user=current_user, musicandauditoryartcard=musicandauditoryartcard)

@views.route('/practice/flashcards/mythology')
@login_required
def flashcards_mythology():
    mythologycard  = Mythologycard.query.order_by(func.random()).limit(1)
    return render_template("practice/flashcards/mythology.html", user=current_user, mythologycard=mythologycard)

@views.route('/practice/flashcards/people')
@login_required
def flashcards_people():
    peoplecard  = Peoplecard.query.order_by(func.random()).limit(1)
    return render_template("practice/flashcards/performance.html", user=current_user, peoplecard=peoplecard)

@views.route('/practice/flashcards/performance')
@login_required
def flashcards_performance():
    performancecard  = Performancecard.query.order_by(func.random()).limit(1)
    return render_template("practice/flashcards/performance.html", user=current_user, performancecard=performancecard)

@views.route('/practice/flashcards/philosophy')
@login_required
def flashcards_philosophy():
    philosophycard  = Philosophycard.query.order_by(func.random()).limit(1)
    return render_template("practice/flashcards/philosophy.html", user=current_user, philosophycard=philosophycard)

@views.route('/practice/flashcards/popular-culture')
@login_required
def flashcards_popular_culture():
    popularculturecard  = Popularculturecard.query.order_by(func.random()).limit(1)
    return render_template("practice/flashcards/popular-culture.html", user=current_user, popularculturecard=popularculturecard)

@views.route('/practice/flashcards/religion')
@login_required
def flashcards_religion():
    religioncard  = Religioncard.query.order_by(func.random()).limit(1)
    return render_template("practice/flashcards/religion.html", user=current_user, religioncard=religioncard)

@views.route('/practice/flashcards/science')
@login_required
def flashcards_science():
    sciencecard  = Sciencecard.query.order_by(func.random()).limit(1)
    return render_template("practice/flashcards/science.html", user=current_user, sciencecard=sciencecard)

@views.route('/practice/flashcards/social-science')
@login_required
def flashcards_social_science():
    socialsciencecard  = Socialsciencecard.query.order_by(func.random()).limit(1)
    return render_template("practice/flashcards/social-science.html", user=current_user, socialsciencecard=socialsciencecard)

@views.route('/practice/flashcards/sports')
@login_required
def flashcards_sports():
    sportscard  = Sportscard.query.order_by(func.random()).limit(1)
    return render_template("practice/flashcards/sports.html", user=current_user, sportscard=sportscard)

@views.route('/practice/flashcards/visual-art')
@login_required
def flashcards_visual_art():
    visualartcard  = Visualartcard.query.order_by(func.random()).limit(1)
    return render_template("practice/flashcards/visual-art.html", user=current_user, visualartcard=visualartcard)