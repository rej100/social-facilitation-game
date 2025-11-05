# Run with: streamlit run Facilitation-game.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

RANDOMIZE_OPTION_ORDER = True

class SocialEntrepreneurGame:
    def __init__(self):
        """Initialize game data for the social entrepreneurship facilitation."""
        self.entrepreneur_profiles = [
            {
                "name": "Amara",
                "archetype": "Social Bricoleur",
                "skills": "Community health navigation and plain-language storytelling",
                "background": (
                    "Former community midwife who lost a neighbour to a preventable birth complication "
                    "and now runs weekly clinic escorts and home check-ins for expectant mothers."
                ),
                "constraints": "Lives on small grants and must juggle caregiving with the support network she coordinates.",
                "strengths": "Families call her first because she knows every local clinic and can improvise workable fixes fast."
            },
            {
                "name": "Mateo",
                "archetype": "Social Constructionist",
                "skills": "Coalition building across schools, businesses, and city agencies",
                "background": (
                    "Former public-school teacher who now coordinates a skills pipeline pairing apprenticeships, "
                    "evening classes, and employer mentors for young people locked out of formal jobs."
                ),
                "constraints": "Has to keep funders, principals, and employers aligned each quarter or commitments fall through.",
                "strengths": "Maps how partners fit together, speaks the language of each sector, and can broker deals quickly."
            },
            {
                "name": "Camille",
                "archetype": "Social Engineer",
                "skills": "Blended finance structuring, housing policy, and coalition bargaining",
                "background": (
                    "Former city redevelopment analyst who founded Keys Forward, a hybrid housing venture that turns vacant "
                    "buildings into permanently affordable homes through community land trusts and municipal guarantees."
                ),
                "constraints": "Every deal requires keeping city councils, impact investors, and resident boards aligned while permits crawl.",
                "strengths": "Braids public and patient capital, earns trust with tenant leaders, and documents playbooks other cities can copy."
            }
        ]

        self.rounds = [
            {
                "title": "Catalyst Moment",
                "description": (
                    "Your venture just hit a tipping point. "
                    "You need to turn the momentum into a concrete mission that focuses on social value, "
                    "while also preparing to implement your plan."
                ),
                "options": [
                    {
                        "title": "Listening tour & story mapping",
                        "description": (
                            "Hold listening circles with local families, staff, and partners to surface blind spots and tighten the mission story."
                        ),
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Amara": {"min": 1.3, "mid": 1.8, "max": 2.3},
                            "Mateo": {"min": 1.0, "mid": 1.4, "max": 1.8},
                            "Camille": {"min": 0.7, "mid": 1.0, "max": 1.4}
                        },
                        "theory": "Portales (2019) emphasises social sensitivity and mission clarity rooted in the community."
                    },
                    {
                        "title": "Secure an early champion investor",
                        "description": (
                            "Approach a values-aligned funder to bankroll early trials, accepting they will want a say in how you operate."
                        ),
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Amara": {"min": 0.5, "mid": 0.8, "max": 1.3},
                            "Mateo": {"min": 1.3, "mid": 1.8, "max": 2.3},
                            "Camille": {"min": 1.0, "mid": 1.5, "max": 2.0}
                        },
                        "theory": "Highlights early resource mobilisation tensions described by Portales (2019)."
                    },
                    {
                        "title": "Design your impact thesis & metrics",
                        "description": (
                            "Work with you stakeholders to draft an impact thesis that combines stories and data, agreeing on what actions would actually trigger changes."
                        ),
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Amara": {"min": 0.9, "mid": 1.2, "max": 1.6},
                            "Mateo": {"min": 1.2, "mid": 1.6, "max": 2.0},
                            "Camille": {"min": 1.3, "mid": 1.8, "max": 2.3}
                        },
                        "theory": "Balancing purpose with accountability corresponds the need for staying disciplined in both the social and commercial aspect (Portales 2019)"
                    }
                ],
                "scenario_update": ""
            },
            {
                "title": "Designing the Intervention",
                "description": (
                    "With your mission defined, it's time to shape how change happens. Choosing the right search process "
                    "and scale of response will determine who you can reach next."
                ),
                "options": [
                    {
                        "title": "Prototype a micro-solution with existing assets",
                        "description": (
                            "Build a lean pilot that stitches together community hacks and idle resources to see if local fixes can scale."
                        ),
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Amara": {"min": 1.3, "mid": 1.8, "max": 2.3},
                            "Mateo": {"min": 1.0, "mid": 1.4, "max": 1.8},
                            "Camille": {"min": 0.7, "mid": 1.0, "max": 1.4}
                        },
                        "theory": "Zahra et al. (2009) describe one of the archetypes as masters of local improvisation."
                    },
                    {
                        "title": "Build a multi-sector service blueprint",
                        "description": (
                            "Decide on roles between NGOs, public agencies, and business partners so everyone knows their job before you build infrastructure."
                        ),
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Amara": {"min": 0.5, "mid": 0.8, "max": 1.3},
                            "Mateo": {"min": 1.3, "mid": 1.8, "max": 2.3},
                            "Camille": {"min": 1.0, "mid": 1.5, "max": 2.0}
                        },
                        "theory": "An archetype focuses on systemic gaps that existing institutions aren't filling (Zahra et al. 2009)"
                    },
                    {
                        "title": "Institutional Listening Tour",
                        "description": (
                            "Create a meeting with frontline staff, city officials, and regulators for a convesation about the problems at hand, then agree on the biggest fixes to go after first."
                        ),
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Amara": {"min": 0.9, "mid": 1.2, "max": 1.6},
                            "Mateo": {"min": 1.2, "mid": 1.6, "max": 2.0},
                            "Camille": {"min": 1.3, "mid": 1.8, "max": 2.3}
                        },
                        "theory": "Zahra et al. (2009) say that careful listening is important for identyfing the parts of the system where small tweaks cause large improvements."
                    }
                ],
                "scenario_update": (
                    "Your early moves are drawing attention. Community partners are watching to see if you stay grounded "
                    "while funders are curious about your path to scale."
                )
            },
            {
                "title": "Resource Strategy & Accountability",
                "description": (
                    "Progress attracts resources, but also scrutiny. How you structure accountability and learning now determines "
                    "whether you can manage the pressure from the dual-mission pressure that Portales (2019) highlights."
                ),
                "options": [
                    {
                        "title": "Establish a shared accountability council",
                        "description": (
                            "Create an accountability council of residents, staff, and funders that challenges decisions in real time, even when it slows things down."
                        ),
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Amara": {"min": 1.3, "mid": 1.8, "max": 2.3},
                            "Mateo": {"min": 1.0, "mid": 1.4, "max": 1.8},
                            "Camille": {"min": 0.7, "mid": 1.0, "max": 1.4}
                        },
                        "theory": "Matches the need for stakeholder dialogue and legitimacy building. (Portales 2019)"
                    },
                    {
                        "title": "Forge a corporate impact partnership",
                        "description": (
                            "Negotiate with a corporate ally for capital and logistics, weighing extra reach against the risks of heavily associating with their brand."
                        ),
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Amara": {"min": 0.5, "mid": 0.8, "max": 1.3},
                            "Mateo": {"min": 1.3, "mid": 1.8, "max": 2.3},
                            "Camille": {"min": 1.0, "mid": 1.5, "max": 2.0}
                        },
                        "theory": "Illustrates the opportunity-risk trade-off when partnering with market actors (Zahra et al., 2009)."
                    },
                    {
                        "title": "Invest in an outcomes learning lab",
                        "description": (
                            "Create a learning lab that runs rapid experiments, tests measures, and shares lessons across your ecosystem."
                        ),
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Amara": {"min": 0.9, "mid": 1.2, "max": 1.6},
                            "Mateo": {"min": 1.2, "mid": 1.6, "max": 2.0},
                            "Camille": {"min": 1.3, "mid": 1.8, "max": 2.3}
                        },
                        "theory": "Supports the adaptive, self-correcting mindset that Portales (2019) and Zahra et al. (2009) describe."
                    }
                ],
                "scenario_update": (
                    "Impact journalists have profiled your progress. Expectations around transparency and measurable progress are rising."
                )
            },
            {
                "title": "Leading for Scale",
                "description": (
                    "Traction now forces leadership evolution. How you structure governance and replication decides whether you can grow "
                    "without losing sight of you social mission."
                ),
                "options": [
                    {
                        "title": "Distribute leadership to local leaders",
                        "description": (
                            "Train local leaders to manage budgets and decisions so leadership stays rooted, accepting that some will do their jobs better than others and instructions might not be followed perfectly."
                        ),
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Amara": {"min": 1.3, "mid": 1.8, "max": 2.3},
                            "Mateo": {"min": 1.0, "mid": 1.4, "max": 1.8},
                            "Camille": {"min": 0.7, "mid": 1.0, "max": 1.4}
                        },
                        "theory": "Necessary leadership changes can hurt \"mission fidelity\" (Portales 2019)"
                    },
                    {
                        "title": "Professionalize operations",
                        "description": (
                            "Hire specialist managers to document processes, tighten compliance, and pursue accreditation."
                        ),
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Amara": {"min": 0.5, "mid": 0.8, "max": 1.3},
                            "Mateo": {"min": 1.3, "mid": 1.8, "max": 2.3},
                            "Camille": {"min": 1.0, "mid": 1.5, "max": 2.0}
                        },
                        "theory": "Supports scaling a benture with stronger formal systems for a type of social entrepreneur focused on building alternative structures (Portales, 2019)."
                    },
                    {
                        "title": "Open-source your playbook",
                        "description": (
                            "Publish your playbook openly so others can adapt it, even if versions appear that don’t match your standards."
                        ),
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Amara": {"min": 0.9, "mid": 1.2, "max": 1.6},
                            "Mateo": {"min": 1.2, "mid": 1.6, "max": 2.0},
                            "Camille": {"min": 1.3, "mid": 1.8, "max": 2.3}
                        },
                        "theory": "Extending ambitions to cause system-wide change (Zahra et al., 2009)."
                    }
                ],
                "scenario_update": (
                    "Regional governments and global networks have noticed your results. Replication requests and compliance checks are piling up."
                )
            },
            {
                "title": "Ethical Crossroads & Legacy",
                "description": (
                    "Long-term stewardship decisions define how your venture sustains social wealth. Each choice tests your values against "
                    "scalability and resilience."
                ),
                "options": [
                    {
                        "title": "Decline misaligned funding & cultivate patient capital",
                        "description": (
                            "Say no to a generous but misaligned funder and focus further on slower, values-first capital so you stay in control."
                        ),
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Amara": {"min": 1.3, "mid": 1.8, "max": 2.3},
                            "Mateo": {"min": 1.0, "mid": 1.4, "max": 1.8},
                            "Camille": {"min": 0.7, "mid": 1.0, "max": 1.4}
                        },
                        "theory": "Reflects the ethical guardrails and mission discipline as mentioned in Portales (2019) and Zahra et al. (2009) discuss."
                    },
                    {
                        "title": "Spin off a revenue-generating unit from the business",
                        "description": (
                            "Launch an income focused arm to subsidise social programs, taking on the distraction of running a fully market focused unit."
                        ),
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Amara": {"min": 0.5, "mid": 0.8, "max": 1.3},
                            "Mateo": {"min": 1.3, "mid": 1.8, "max": 2.3},
                            "Camille": {"min": 1.0, "mid": 1.5, "max": 2.0}
                        },
                        "theory": "Showcases the tension between sustaining economic and social wealth in later stages (Portales, 2019)."
                    },
                    {
                        "title": "Pursue policy reform that could disrupt operations",
                        "description": (
                            "Use your influence to push for policy changes that would reset the system, knowing it could make your current business model obsolete."
                        ),
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Amara": {"min": 0.9, "mid": 1.2, "max": 1.6},
                            "Mateo": {"min": 1.2, "mid": 1.6, "max": 2.0},
                            "Camille": {"min": 1.3, "mid": 1.8, "max": 2.3}
                        },
                        "theory": "Some social entrepreneurs are more susceptible to systemic risks. (Zahra et al. 2009)"
                    }
                ],
                "scenario_update": (
                    "Investors, policy makers, and community allies are all watching your next move to see what type of legacy you decide one."
                )
            }
        ]


def initialize_session_state():
    """Initialize all session state variables needed for the game."""
    if "game_stage" not in st.session_state:
        st.session_state.game_stage = "setup"

    if "teams" not in st.session_state:
        st.session_state.teams = []

    if "team_points" not in st.session_state:
        st.session_state.team_points = {}

    if "team_entrepreneurs" not in st.session_state:
        st.session_state.team_entrepreneurs = {}

    if "team_history" not in st.session_state:
        st.session_state.team_history = {}

    if "current_round" not in st.session_state:
        st.session_state.current_round = 1

    if "total_rounds" not in st.session_state:
        st.session_state.total_rounds = 5

    if "active_team" not in st.session_state:
        st.session_state.active_team = 0

    if "round_completed" not in st.session_state:
        st.session_state.round_completed = False


def setup_teams():
    """Screen for setting up team names and assigning entrepreneurs."""
    st.title("Who is the Social Entrepreneur?")
    st.write("### Team Formation")

    game = SocialEntrepreneurGame()

    entrepreneur_images = {
        "Amara": "images/amara.png",
        "Mateo": "images/mateo.png",
        "Camille": "images/camille.png"
    }

    col1, col2 = st.columns(2)

    team_names = []
    num_profiles = len(game.entrepreneur_profiles)

    for i in range(num_profiles):
        container = col1 if i < 2 else col2

        with container:
            st.markdown(f"### Team {i + 1}")
            name = st.text_input(f"Team {i + 1} Name:", value=f"Team {i + 1}", key=f"team_{i}_name")
            team_names.append(name)

            entrepreneur = game.entrepreneur_profiles[i]

            img_col, info_col = st.columns([1, 3])

            with img_col:
                try:
                    st.image(entrepreneur_images[entrepreneur["name"]], width=100)
                except Exception:
                    st.write("🧭")

            with info_col:
                st.markdown(f"**Entrepreneur:** {entrepreneur['name']}")
                st.markdown(f"**Approach:** {entrepreneur['archetype']}")
                st.markdown(f"**Mission Focus:** {entrepreneur['skills']}")
                st.caption(entrepreneur["background"])

            st.markdown("---")

    if st.button("Start Game", type="primary"):
        st.session_state.teams = team_names

        for i, team in enumerate(team_names):
            st.session_state.team_points[team] = 10
            st.session_state.team_entrepreneurs[team] = game.entrepreneur_profiles[i]["name"]
            st.session_state.team_history[team] = []

        st.session_state.game_stage = "intro"
        st.rerun()


def show_introduction():
    """Introduction screen with game overview and rules."""
    st.title("Who is the Social Entrepreneur?")

    st.markdown(
        """
        ## Welcome to the Impact Studio

        ### Game Overview
        Each team plays as a different social entrepreneur archetype from Zahra et al. (2009) and Portales (2019).
        Your task is to navigate decisions that focus on social value creation and the sustainability of the organisation.

        ### Game Rules
        1. Teams begin with **10 shared impact points**.
        2. Every round you pick **one strategic move** and decide how many points (max 5) to invest.
        3. Outcomes depend on how well the move aligns with your entrepreneur’s archetype, investment level, and theory fit.
        4. Skipping a round allows you to save your points, but you miss out on any potential gains.
        5. The team with the highest impact points at the end wins!

        ### Concepts to Watch
        - Mission vs. Market tension and accountability concerns (Portales, 2019)
        - Typologies: Social Bricoleur, Constructionist, Engineer (Zahra et al., 2009)
        - Leadership evolution and ethical concerns as ventures become succesful (Portales, 2019; Zahra et al., 2009)
        """
    )

    if st.button("Begin Briefing", type="primary"):
        st.session_state.game_stage = "briefing"
        st.rerun()


def show_briefing():
    """Show contextual briefing for the facilitation."""
    st.title("Briefing: The Social Entrepreneur Studio")

    st.markdown(
        """
        You are at the Social Entrepreneur Studio, a gathering where community leaders, funders, and policy shapers
        search for ventures that can make real social impact. The studio is monitoring three real-time ventures.

        Your team acts as the venture's leadership circle. Every choice you make is broadcast to the studio,
        showcasing different ideas from the readings.
        """
    )

    if st.button("Enter Round 1", type="primary", key="start_rounds_btn"):
        st.session_state.game_stage = "round_1"
        st.session_state.active_team = 0
        st.rerun()


def run_game_round(round_number: int):
    """Run a single round of the game."""
    team_index = st.session_state.active_team
    current_team = st.session_state.teams[team_index]
    entrepreneur_name = st.session_state.team_entrepreneurs[current_team]
    current_points = st.session_state.team_points[current_team]

    game = SocialEntrepreneurGame()
    round_data = game.rounds[round_number - 1]

    st.title(f"Round {round_number}: {round_data['title']}")
    st.subheader(f"{current_team}'s Turn ({entrepreneur_name})")

    col1, col2 = st.columns(2)
    with col1:
        st.info(f"Impact points available: {current_points}")
    with col2:
        st.warning("⚠️ You can allocate at most 5 impact points.")

    st.markdown("### Scenario")
    st.markdown(round_data["description"])

    if round_number > 1:
        st.warning(f"**Studio Update:** {round_data['scenario_update']}")

    round_key = f"round_{round_number}_team_{team_index}"
    if f"{round_key}_selected_option" not in st.session_state:
        st.session_state[f"{round_key}_selected_option"] = None
    order_key = f"round_{round_number}_option_order"
    if order_key not in st.session_state:
        indices = list(range(len(round_data["options"])))
        if RANDOMIZE_OPTION_ORDER:
            random.shuffle(indices)
        st.session_state[order_key] = indices

    if current_points <= 0:
        st.error("No impact points left. You must pass this round.")
        if st.button("Skip Turn", key=f"skip_zero_{round_number}_{team_index}"):
            st.session_state.active_team = (team_index + 1) % len(st.session_state.teams)

            if st.session_state.active_team == 0:
                if round_number < st.session_state.total_rounds:
                    st.session_state.game_stage = f"round_{round_number + 1}"
                else:
                    st.session_state.game_stage = "results"
            st.rerun()
        return

    st.markdown("### Strategic Options")

    if st.session_state[f"{round_key}_selected_option"] is None:
        option_order = st.session_state[order_key]
        cols = st.columns(len(option_order))

        for display_idx, (col, option_index) in enumerate(zip(cols, option_order)):
            option = round_data["options"][option_index]
            with col:
                st.markdown(f"**Option {display_idx + 1}: {option['title']}**")
                st.markdown(option["description"])

                min_points = min(option["points_range"][0], 5)
                max_points = min(option["points_range"][1], 5)
                st.markdown(f"*Investment window: {min_points}-{max_points} impact points*")

                if st.button(
                    f"Choose Option {display_idx + 1}",
                    key=f"option_{round_number}_{team_index}_{option_index}"
                ):
                    st.session_state[f"{round_key}_selected_option"] = option_index
                    st.rerun()

    if st.session_state[f"{round_key}_selected_option"] is not None:
        selected_option = st.session_state[f"{round_key}_selected_option"]
        selected_option_data = round_data["options"][selected_option]

        original_min, original_max = selected_option_data["points_range"]
        min_points = min(original_min, 5)
        max_points = min(original_max, 5)

        st.markdown(f"### Selected Strategy: {selected_option_data['title']}")
        st.markdown(selected_option_data["description"])

        min_points = min(min_points, current_points)
        max_points = min(max_points, current_points, 5)
        if min_points > max_points:
            min_points = max_points

        st.markdown("#### Allocate your impact points")

        if min_points < max_points:
            invested_points = st.slider(
                "Impact points to commit:",
                min_value=min_points,
                max_value=max_points,
                value=min_points,
                step=1
            )
        else:
            invested_points = min_points
            st.markdown(f"You can only commit **{min_points}** impact points this turn.")

        st.progress(invested_points / 5)
        st.caption("Outcome details appear after you confirm. Watch the sidebar for score updates.")

        st.markdown("#### Theory in Play")
        st.info(selected_option_data["theory"])

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Choose Different Option", key=f"change_option_{round_number}_{team_index}"):
                st.session_state[f"{round_key}_selected_option"] = None
                st.rerun()

        with col2:
            if st.button("Confirm Decision", key=f"confirm_{round_number}_{team_index}", type="primary"):
                outcome_mapping = selected_option_data["outcome_mapping"][entrepreneur_name]

                if max_points == min_points:
                    multiplier = outcome_mapping["min"]
                else:
                    relative_investment = (invested_points - min_points) / (max_points - min_points)
                    if relative_investment <= 0.33:
                        multiplier = outcome_mapping["min"]
                    elif relative_investment <= 0.66:
                        multiplier = outcome_mapping["mid"]
                    else:
                        multiplier = outcome_mapping["max"]

                outcome_points = round(invested_points * multiplier)

                new_points = current_points - invested_points + outcome_points
                st.session_state.team_points[current_team] = new_points

                st.session_state.team_history[current_team].append(
                    {
                        "round": round_number,
                        "option": selected_option_data["title"],
                        "invested": invested_points,
                        "gained": outcome_points,
                        "net": outcome_points - invested_points,
                        "multiplier": multiplier
                    }
                )

                st.session_state[f"{round_key}_selected_option"] = None

                st.session_state.active_team = (team_index + 1) % len(st.session_state.teams)

                if st.session_state.active_team == 0:
                    st.session_state.pop(order_key, None)
                    if round_number < st.session_state.total_rounds:
                        st.session_state.game_stage = f"round_{round_number + 1}"
                    else:
                        st.session_state.game_stage = "results"

                st.rerun()

    if st.button("Skip this round (bank points)", key=f"skip_normal_{round_number}_{team_index}"):
        st.session_state.team_history[current_team].append(
            {
                "round": round_number,
                "option": "Skipped round",
                "invested": 0,
                "gained": 0,
                "net": 0,
                "multiplier": None
            }
        )

        st.session_state.active_team = (team_index + 1) % len(st.session_state.teams)

        if st.session_state.active_team == 0:
            st.session_state.pop(order_key, None)
            if round_number < st.session_state.total_rounds:
                st.session_state.game_stage = f"round_{round_number + 1}"
            else:
                st.session_state.game_stage = "results"
        st.rerun()


def show_results():
    """Display final results and winner."""
    st.title("Impact Outcomes")

    results = []
    for team in st.session_state.teams:
        results.append(
            {
                "Team": team,
                "Entrepreneur": st.session_state.team_entrepreneurs[team],
                "Impact Points": st.session_state.team_points[team],
                "Starting Impact": 10,
                "Net Impact": st.session_state.team_points[team] - 10
            }
        )

    results_df = pd.DataFrame(results).sort_values("Impact Points", ascending=False)

    winner = results_df.iloc[0]["Team"]
    winner_points = results_df.iloc[0]["Impact Points"]
    winner_entrepreneur = results_df.iloc[0]["Entrepreneur"]

    st.balloons()
    st.markdown(f"## 🏆 Studio Standout: {winner}")
    st.markdown(f"### Archetype: {winner_entrepreneur}")
    st.markdown(f"### Final Impact Points: {winner_points}")

    st.markdown("## Final Rankings")

    colors = ["#2E8B57", "#4682B4", "#CD853F", "#708090"]

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(
        results_df["Team"],
        results_df["Impact Points"],
        color=[colors[i] if i < len(colors) else "#A9A9A9" for i in range(len(results_df))]
    )

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + 1,
            f"{height}",
            ha="center",
            va="bottom"
        )

    ax.set_ylabel("Impact Points")
    ax.set_title("Team Impact Outcomes")
    ax.set_ylim(0, max(results_df["Impact Points"]) * 1.2)

    st.pyplot(fig)

    st.markdown("## Detailed Results")
    st.table(results_df)

    st.markdown("## Decision Log")
    for team in st.session_state.teams:
        with st.expander(f"{team} ({st.session_state.team_entrepreneurs[team]})"):
            history = st.session_state.team_history[team]
            if not history:
                st.write("No decisions recorded.")
            else:
                for decision in history:
                    st.markdown(f"**Round {decision['round']}:** {decision['option']}")
                    st.markdown(
                        f"Invested: {decision['invested']} | Outcome: {decision['gained']} | "
                        f"Net: {decision['net']} | Multiplier: {decision['multiplier'] if decision['multiplier'] is not None else '—'}"
                    )
                    st.markdown("---")

    st.markdown("## Key Insights from the Readings")

    with st.expander("What differentiates social entrepreneurs? (Portales, 2019)"):
        st.markdown(
            """
            - Social entrepreneurs focus on social value propositions while sustaining economic viability.
            - They manage tensions between mission fidelity and market realities with accountability practices.
            - Leadership must evolve from founder-centric drive to distributed leadership as the venture matures.
            """
        )

    with st.expander("Typology of change agents (Zahra et al., 2009)"):
        st.markdown(
            """
            - Social Bricoleurs leverage tacit, local knowledge to tackle specific needs.
            - Social Constructionists orchestrate partners and scale services to close market gaps.
            - Social Engineers attempt systemic redesign, accepting higher ethical and political exposure.
            """
        )

    st.markdown("## Discussion Prompts")
    st.markdown(
        """
        1. How did your archetype's strengths and constraints inform the decisions you felt confident making?
        2. Where did you experience mission–market or ethical tensions, and how did the readings help you make you decision?
        3. If you had another round, what governance or leadership shift would you prioritise to sustain social wealth?
        4. How can allies (funders, policymakers, corporates) recognise and support different archetypes without forcing convergence?
        """
    )

    if st.button("Play Again"):
        st.session_state.clear()
        st.rerun()


def display_sidebar_info():
    """Display team information in the sidebar."""
    if st.session_state.game_stage not in ["setup", "intro", "briefing", "results"]:
        st.sidebar.title("Impact Tracker")

        game = SocialEntrepreneurGame()
        profile_map = {p["name"]: p for p in game.entrepreneur_profiles}

        entrepreneur_images = {
            "Amara": "images/amara.png",
            "Mateo": "images/mateo.png",
            "Camille": "images/camille.png"
        }

        for team in st.session_state.teams:
            entrepreneur = st.session_state.team_entrepreneurs[team]
            points = st.session_state.team_points[team]
            profile = profile_map.get(entrepreneur, {})

            img_col, info_col = st.sidebar.columns([1, 3])

            with img_col:
                try:
                    st.image(entrepreneur_images[entrepreneur], width=50)
                except Exception:
                    st.write("🧭")

            with info_col:
                if team == st.session_state.teams[st.session_state.active_team]:
                    st.markdown(f"### → {team}")
                    st.markdown(f"**Impact Points: {points}**")
                else:
                    st.markdown(f"### {team}")
                    st.markdown(f"Impact Points: {points}")

                if profile:
                    st.caption(profile.get("archetype", ""))

            st.sidebar.markdown("---")

        st.sidebar.markdown(f"**Round:** {st.session_state.current_round} / {st.session_state.total_rounds}")


def main():
    """Main entry point for the application."""
    st.set_page_config(page_title="Who is the Social Entrepreneur?", layout="wide")

    initialize_session_state()
    display_sidebar_info()

    if st.session_state.game_stage == "setup":
        setup_teams()
    elif st.session_state.game_stage == "intro":
        show_introduction()
    elif st.session_state.game_stage == "briefing":
        show_briefing()
    elif st.session_state.game_stage == "round_1":
        st.session_state.current_round = 1
        run_game_round(1)
    elif st.session_state.game_stage == "round_2":
        st.session_state.current_round = 2
        run_game_round(2)
    elif st.session_state.game_stage == "round_3":
        st.session_state.current_round = 3
        run_game_round(3)
    elif st.session_state.game_stage == "round_4":
        st.session_state.current_round = 4
        run_game_round(4)
    elif st.session_state.game_stage == "round_5":
        st.session_state.current_round = 5
        run_game_round(5)
    elif st.session_state.game_stage == "results":
        show_results()


if __name__ == "__main__":
    main()
