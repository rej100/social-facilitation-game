# Instructions to start the game
# 1: Make sure all libraties are installed;
# 2: Run the following command in your terminal after running the code: streamlit run GAME.py

# lIBRARIES:

import streamlit as st
import random
import pandas as pd
import time
import matplotlib.pyplot as plt
import base64

class InformalEntrepreneurGame:
    def __init__(self):
        """Initialize the game components"""
        self.entrepreneur_profiles = [
            {
                "name": "Maria",
                "skills": "Cooking & food preparation",
                "background": "Single mother with two children, learned cooking from her grandmother",
                "constraints": "Limited startup capital, needs to work close to home to care for children",
                "strengths": "Strong community ties, excellent culinary skills"
            },
            {
                "name": "Carlos",
                "skills": "Technical repair & electronics",
                "background": "Former factory worker, self-taught in electronics repair",
                "constraints": "No formal certification, limited tools",
                "strengths": "Problem-solving ability, extensive knowledge of local supply chains"
            },
            {
                "name": "Aisha",
                "skills": "Tailoring & textile work",
                "background": "Rural migrant with traditional craft skills",
                "constraints": "New to the city, limited social network",
                "strengths": "Unique craft techniques, highly adaptable"
            },
            {
                "name": "Miguel",
                "skills": "Transportation & deliveries",
                "background": "Has owned the same motorcycle for 10 years, knows the city perfectly",
                "constraints": "No driver's license, motorcycle needs frequent repairs",
                "strengths": "Knowledge of all city streets and shortcuts, trusted by local vendors"
            }
        ]
        
        self.rounds = [
            {
                "title": "Getting Started",
                "description": "You're trying to establish your informal business in the neighborhood. With limited resources, you need to make strategic choices about how to begin.",
                "options": [
                    {
                        "title": "Invest in basic tools/equipment",
                        "description": "Spend points on essential tools and equipment to provide your service/product",
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Maria": {"min": 0.8, "mid": 1.5, "max": 2.0},  # Maria can lose with small investment
                            "Carlos": {"min": 1.2, "mid": 2.0, "max": 2.5}, # Carlos thrives with tools
                            "Aisha": {"min": 0.7, "mid": 1.5, "max": 2.0},  # Aisha can lose with small investment
                            "Miguel": {"min": -0.2, "mid": 0.3, "max": 1.5}  # Miguel can lose significantly on tools
                        },
                        "theory": "Bricolage (Imas et al., 2012) - Making do with limited resources"
                    },
                    {
                        "title": "Build social connections",
                        "description": "Spend time and resources building relationships with potential customers and other vendors",
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Maria": {"min": 1.2, "mid": 2.0, "max": 2.5},  # Maria thrives with social connections #
                            "Carlos": {"min": 0.8, "mid": 1.5, "max": 2.0}, # Carlos is less socially adept
                            "Aisha": {"min": -0.3, "mid": 0.5, "max": 1.5},  # Aisha struggles with social connections
                            "Miguel": {"min": 1.2, "mid": 2.0, "max": 2.5} # Miguel benefits greatly from social ties
                        },
                        "theory": "Social embeddedness (Imas et al., 2012) - Leveraging social capital"
                    },
                    {
                        "title": "Scope out locations",
                        "description": "Invest time finding strategic locations to operate with good customer flow but minimal interference from authorities",
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Maria": {"min": 0.8, "mid": 1.5, "max": 2.0}, # Maria does okay with location scouting
                            "Carlos": {"min": -0.5, "mid": 0.5, "max": 1.5},  # Carlos is bad at location scouting
                            "Aisha": {"min": 0.8, "mid": 1.5, "max": 2.0}, # Aisha does okay with location scouting 
                            "Miguel": {"min": 1.2, "mid": 2.0, "max": 2.5} #     Miguel excels at finding good locations
                        },
                        "theory": "Institutional avoidance (Webb et al., 2009) - Finding spaces between formal institutions"
                    }
                ],
                "scenario_update": "The city authorities have announced increased patrols targeting informal vendors. Some locations have become riskier than others."
            },
            {
                "title": "Facing Competition",
                "description": "After a few weeks of operation, you're facing competition from both formal businesses and other informal entrepreneurs.",
                "options": [
                    {
                        "title": "Lower prices",
                        "description": "Reduce your margins to attract more customers",
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Maria": {"min": -0.5, "mid": 0.2, "max": 1.0},  # Maria can lose badly on price competition
                            "Carlos": {"min": 0.0, "mid": 0.7, "max": 1.3}, # Carlos is somewhat resilient to price competition
                            "Aisha": {"min": -0.5, "mid": 0.2, "max": 1.0},  # Aisha also vulnerable on price
                            "Miguel": {"min": 0.0, "mid": 1.0, "max": 1.3} # Miguel can hold steady with price cuts 
                        },
                        "theory": "Necessity-driven strategy (Salvi et al., 2023) - Short-term survival focus"
                    },
                    {
                        "title": "Differentiate your offering",
                        "description": "Invest in creating a unique service or product that others don't provide",
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Maria": {"min": 1.5, "mid": 1.8, "max": 2.2}, # Maria can innovate well
                            "Carlos": {"min": 1.2, "mid": 1.5, "max": 1.8}, # Carlos can innovate moderately
                            "Aisha": {"min": 1.5, "mid": 2.0, "max": 2.5}, # Aisha can innovate well
                            "Miguel": {"min": 1.0, "mid": 1.2, "max": 1.5} # Miguel has limited innovation capacity
                        },
                        "theory": "Opportunity-driven strategy (Salvi et al., 2023) - Innovation focus"
                    },
                    {
                        "title": "Form alliances",
                        "description": "Collaborate with complementary businesses to offer joint services",
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Maria": {"min": 1.2, "mid": 1.5, "max": 1.8}, # Maria can build strong alliances
                            "Carlos": {"min": 1.0, "mid": 1.2, "max": 1.5}, # Carlos can form basic partnerships
                            "Aisha": {"min": 1.0, "mid": 1.2, "max": 1.5}, # Aisha can collaborate effectively
                            "Miguel": {"min": 1.5, "mid": 1.8, "max": 2.2} # Miguel excels in forming strategic alliances
                        },
                        "theory": "Collective action (Imas et al., 2012) - Strength through collaboration"
                    }
                ],
                "scenario_update": "A large corporate chain has opened nearby and is attracting many customers with standardized offerings and lower prices."
            },
            {
                "title": "Institutional Pressure",
                "description": "Local authorities are increasingly enforcing regulations against informal businesses. You need to respond to this institutional pressure.",
                "options": [
                    {
                        "title": "Partial formalization",
                        "description": "Obtain some basic permits while keeping aspects of your business informal",
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Maria": {"min": 1.0, "mid": 1.5, "max": 2.0}, # Maria can benefit from partial formalization
                            "Carlos": {"min": 0.8, "mid": 1.2, "max": 1.5}, # Carlos is somewhat resilient to institutional pressure
                            "Aisha": {"min": 1.0, "mid": 1.5, "max": 2.0}, # Aisha can adapt to formalization
                            "Miguel": {"min": 0.7, "mid": 1.0, "max": 1.3}  # Miguel has limited capacity for formalization
                        },
                        "theory": "Growth-oriented strategy (Salvi et al., 2023) - Step toward formality"
                    },
                    {
                        "title": "Increase community legitimacy",
                        "description": "Strengthen relationships with local community members who can vouch for and protect your business",
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Maria": {"min": 1.5, "mid": 1.8, "max": 2.2}, # Maria has strong community ties
                            "Carlos": {"min": 1.0, "mid": 1.3, "max": 1.6}, # Carlos can build community support
                            "Aisha": {"min": 0.8, "mid": 1.2, "max": 1.5}, # Aisha has moderate community connections
                            "Miguel": {"min": 1.2, "mid": 1.6, "max": 2.0}  # Miguel can leverage community relationships
                        },
                        "theory": "Legitimacy through normative alignment (Webb et al., 2009)"
                    },
                    {
                        "title": "Adapt operations",
                        "description": "Change your hours, location, or methods to avoid enforcement while maintaining your customer base",
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Maria": {"min": 1.0, "mid": 1.3, "max": 1.6}, # Maria can adapt operations moderately
                            "Carlos": {"min": 1.2, "mid": 1.5, "max": 1.8}, # Carlos can adapt operations well
                            "Aisha": {"min": 1.2, "mid": 1.5, "max": 1.8}, # Aisha can adapt operations well
                            "Miguel": {"min": 1.5, "mid": 1.8, "max": 2.2}  # Miguel can adapt operations effectively
                        },
                        "theory": "Permanently informal strategy (Salvi et al., 2023) - Strategic informality"
                    }
                ],
                "scenario_update": "A community organization has formed to advocate for the rights of informal entrepreneurs and is gaining political support."
            },
            {
                "title": "Growth Opportunity",
                "description": "Your business has survived the initial challenges and now has an opportunity to grow. How will you approach this growth phase?",
                "options": [
                    {
                        "title": "Expand current operations",
                        "description": "Invest in expanding your informal business in its current form",
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Maria": {"min": 1.3, "mid": 1.6, "max": 2.0}, # Maria can grow well informally
                            "Carlos": {"min": 1.2, "mid": 1.5, "max": 1.8}, # Carlos can grow well informally
                            "Aisha": {"min": 1.3, "mid": 1.6, "max": 2.0}, # Aisha can grow well informally
                            "Miguel": {"min": 1.0, "mid": 1.3, "max": 1.6}  # Miguel can grow well informally
                        },
                        "theory": "Permanently informal strategy (Salvi et al., 2023) - Strategic choice to remain informal"
                    },
                    {
                        "title": "Transition toward formality",
                        "description": "Begin the process of registering your business and complying with regulations",
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Maria": {"min": 1.0, "mid": 1.5, "max": 2.0}, # Maria can benefit from formalization
                            "Carlos": {"min": 1.3, "mid": 1.8, "max": 2.3}, # Carlos can benefit from formalization
                            "Aisha": {"min": 1.2, "mid": 1.7, "max": 2.2}, # Aisha can benefit from formalization
                            "Miguel": {"min": 0.8, "mid": 1.2, "max": 1.6}  # Miguel can benefit from formalization
                        },
                        "theory": "Growth-oriented strategy (Salvi et al., 2023) - Using informality as stepping stone"
                    },
                    {
                        "title": "Form a cooperative",
                        "description": "Join with other informal entrepreneurs to create a cooperative with shared resources",
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Maria": {"min": 1.5, "mid": 2.0, "max": 2.5}, # Maria benefits greatly from collective action 
                            "Carlos": {"min": 1.2, "mid": 1.5, "max": 1.8}, # Carlos benefits from collective action
                            "Aisha": {"min": 1.3, "mid": 1.6, "max": 2.0}, # Aisha benefits from collective action
                            "Miguel": {"min": 1.3, "mid": 1.6, "max": 2.0}  # Miguel benefits from collective action
                        },
                        "theory": "Collective action and social embeddedness (Imas et al., 2012)"
                    }
                ],
                "scenario_update": "Local government has announced a new microenterprise development program that offers support for small businesses willing to formalize."
            },
            {
                "title": "Legacy and Sustainability",
                "description": "Your business has become established in the community. Now you need to consider its long-term sustainability and your legacy as an entrepreneur in the informal economy.",
                "options": [
                    {
                        "title": "Mentor new entrepreneurs",
                        "description": "Dedicate resources to training and supporting other aspiring informal entrepreneurs in your community",
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Maria": {"min": 1.5, "mid": 2.0, "max": 2.4},  # Maria's community connections amplify this
                            "Carlos": {"min": 1.2, "mid": 1.5, "max": 1.8},  # Carlos can effectively transfer technical knowledge
                            "Aisha": {"min": 1.0, "mid": 1.4, "max": 1.8},  # Aisha's craft skills valuable but harder to teach
                            "Miguel": {"min": 0.8, "mid": 1.2, "max": 1.5}   # Miguel's knowledge is very location-specific
                        },
                        "theory": "Social embeddedness and knowledge sharing (Imas et al., 2012) - Creating sustainable informal ecosystems"
                    },
                    {
                        "title": "Technological adaptation",
                        "description": "Adopt new technologies that could transform your informal business model and practices",
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Maria": {"min": 0.5, "mid": 1.0, "max": 1.5},  # Maria's business less tech-dependent
                            "Carlos": {"min": 1.8, "mid": 2.2, "max": 2.6},  # Carlos thrives with technology
                            "Aisha": {"min": 1.0, "mid": 1.5, "max": 2.0},  # Aisha can benefit from digital marketplaces
                            "Miguel": {"min": 1.0, "mid": 1.3, "max": 1.6}   # Miguel can use apps for delivery coordination
                        },
                        "theory": "Opportunity-driven entrepreneurship in digital informality (Salvi et al., 2023) - Adapting informal practices to digital transformation"
                    },
                    {
                        "title": "Build informal-formal bridges",
                        "description": "Create partnerships with formal businesses or institutions while maintaining your informal flexibility",
                        "points_range": (1, 5),
                        "outcome_mapping": {
                            "Maria": {"min": 1.3, "mid": 1.6, "max": 2.0},  # Maria can supply food to formal establishments
                            "Carlos": {"min": 1.5, "mid": 1.8, "max": 2.1},  # Carlos can service equipment for formal businesses
                            "Aisha": {"min": 1.4, "mid": 1.8, "max": 2.2},  # Aisha's crafts can be sold in formal retail
                            "Miguel": {"min": 0.7, "mid": 1.0, "max": 1.5}   # Miguel faces more regulatory hurdles
                        },
                        "theory": "Institutional boundary spanning (Webb et al., 2009) - Creating legitimacy while retaining informality advantages"
                    }
                ],
                "scenario_update": "A business school has started studying successful informal businesses in your city as examples of entrepreneurial resilience. Your business has been recognized for its innovative approach and community impact."
            }
        ]
        
def initialize_session_state():
    """Initialize all session state variables needed for the game"""
    if 'game_stage' not in st.session_state:
        st.session_state.game_stage = 'setup'  # setup, intro, round_1, round_2, round_3, round_4, results
    
    if 'teams' not in st.session_state:
        st.session_state.teams = []  # List of team names
    
    if 'team_points' not in st.session_state:
        st.session_state.team_points = {}  # Dict mapping team names to current points
    
    if 'team_entrepreneurs' not in st.session_state:
        st.session_state.team_entrepreneurs = {}  # Dict mapping team names to assigned entrepreneurs
    
    if 'team_history' not in st.session_state:
        st.session_state.team_history = {}  # Dict mapping team names to list of previous choices
    
    if 'current_round' not in st.session_state:
        st.session_state.current_round = 1  # Current round number
    
    if 'total_rounds' not in st.session_state:
        st.session_state.total_rounds = 5  # Change from 4 to 5
    
    if 'active_team' not in st.session_state:
        st.session_state.active_team = 0  # Index of the currently active team
    
    if 'round_completed' not in st.session_state:
        st.session_state.round_completed = False  # Whether current round is completed

def setup_teams():
    """Screen for setting up team names and assigning entrepreneurs"""
    st.title("Informal Entrepreneurship Game")
    st.write("### Team Setup")
    

    game = InformalEntrepreneurGame()
    
    entrepreneur_images = {
        "Maria": "images/maria.png",
        "Carlos": "images/carlos.png",
        "Aisha": "images/aisha.png",
        "Miguel": "images/miguel.png"
    }
    
    col1, col2 = st.columns(2)
    
    team_names = []
    for i in range(4):
        if i < 2:
            container = col1
        else:
            container = col2
            
        with container:
            st.markdown(f"### Team {i+1}")
            name = st.text_input(f"Team {i+1} Name:", value=f"Team {i+1}", key=f"team_{i}_name")
            team_names.append(name)
            
    
            entrepreneur = game.entrepreneur_profiles[i]
            
            
            img_col, info_col = st.columns([1, 3])
            
            with img_col:
                try:
                    st.image(entrepreneur_images[entrepreneur['name']], width=100)
                except Exception as e:
                    st.write("📝") # Fallback if image not found
            
            with info_col:
                st.markdown(f"**Entrepreneur:** {entrepreneur['name']}")
                st.markdown(f"**Skills:** {entrepreneur['skills']}")
                st.markdown(f"**Background:** {entrepreneur['background']}")
            
            st.markdown("---")
    
    if st.button("Start Game", type="primary"):
       
        st.session_state.teams = team_names
        
        for i, team in enumerate(team_names):
            st.session_state.team_points[team] = 10
            st.session_state.team_entrepreneurs[team] = game.entrepreneur_profiles[i]["name"]
            st.session_state.team_history[team] = []
        
        st.session_state.game_stage = 'intro'
        st.rerun()

def show_introduction():
    """Introduction screen with game overview and rules"""
    st.title("Informal Entrepreneurship Game")
    
    st.markdown("""
    ## Welcome to the Informal Entrepreneurship Challenge!

    ### Game Overview
    In this simulation, each team represents an informal entrepreneur in the same impoverished city. 
    You'll make strategic decisions about how to establish and grow your informal business while 
    navigating institutional, resource, and market challenges.

    ### Game Rules
    1. Each team starts with **10 points total** for the entire game
    2. You must carefully manage your limited resources across all rounds
    3. **Maximum 5 points can be spent per option**
    4. Each round presents a scenario and strategic options
    5. Teams must decide how many points to invest in their chosen strategy
    6. Points invested are multiplied by factors that depend on:
       - How well the strategy fits your entrepreneur's profile
       - The amount of points invested
       - Alignment with effective informal entrepreneurship practices
    7. **Caution:** Poor strategic choices can result in LOSING points!
    8. Being resourceful with your limited points is key to success!
    9. The team with the most points at the end wins!

    ### Key Concepts to Remember
    - **Necessity vs. Opportunity-driven entrepreneurship** (Salvi et al., 2023)
    - **Barefoot entrepreneurship strategies** like bricolage and social embeddedness (Imas et al., 2012)
    - **Institutional alignment** for legitimacy (Webb et al., 2009)
    """)
    
    
    if st.button("Begin Round 1", type="primary"):
        st.session_state.game_stage = 'city_intro'  # Changed from 'round_1' to 'city_intro'
        st.rerun()

def show_city_intro():
    """Show an introduction to the fictional city where the game takes place"""
    st.title("Welcome to Los Santos")
    
    st.markdown("""
    ## LOS SANTOS
    
    A city of **extremes**. Gleaming skyscrapers tower over sprawling shanty towns.
    
    By day, corporate suits chase millions. By night, street vendors hustle for pennies.
    
    The informal economy isn't just surviving here—it's **thriving**. Over 60% of residents make 
    their living outside the system, creating an underground network of goods and services that 
    keeps Los Santos breathing.
    
    The authorities? They look the other way... until they don't.
    
    **Welcome to the hustle.**
    """)
    
    if st.button("Begin Your Journey", type="primary", key="start_journey_btn"):
        # Move to the first round
        st.session_state.game_stage = 'round_1'
        st.session_state.active_team = 0  # Start with the first team
        st.rerun()

def run_game_round(round_number):
    """Run a single round of the game"""
    
    team_index = st.session_state.active_team
    current_team = st.session_state.teams[team_index]
    entrepreneur_name = st.session_state.team_entrepreneurs[current_team]
    current_points = st.session_state.team_points[current_team]
    
    game = InformalEntrepreneurGame()
    round_data = game.rounds[round_number - 1]  # Adjust for 0-based indexing
    
 
    st.title(f"Round {round_number}: {round_data['title']}")
    st.subheader(f"{current_team}'s Turn ({entrepreneur_name})")
    

    col1, col2 = st.columns(2)
    with col1:
        st.info(f"Available points: {current_points}")
    with col2:
        st.warning("⚠️ Maximum 5 points per option")
    
 
    st.markdown("### Scenario")
    st.markdown(round_data["description"])
    
    
    if round_number > 1:
        st.warning(f"**Update:** {round_data['scenario_update']}")
    

    round_key = f"round_{round_number}_team_{team_index}"
    if f"{round_key}_selected_option" not in st.session_state:
        st.session_state[f"{round_key}_selected_option"] = None
    
    
    if current_points <= 0:
        st.error("You've run out of points! You'll need to skip this round.")
        if st.button("Skip Turn", key=f"skip_zero_{round_number}_{team_index}"):
            
            st.session_state.active_team = (team_index + 1) % len(st.session_state.teams)
        
            if st.session_state.active_team == 0:
                if round_number < st.session_state.total_rounds:
                    st.session_state.game_stage = f'round_{round_number + 1}'
                else:
                    st.session_state.game_stage = 'results'
            st.rerun()
        return
    
   
    st.markdown("### Strategic Options")
    

    if st.session_state[f"{round_key}_selected_option"] is None:
        
        cols = st.columns(len(round_data["options"]))
        
        for i, (col, option) in enumerate(zip(cols, round_data["options"])):
            with col:
                st.markdown(f"**Option {i+1}: {option['title']}**")
                st.markdown(option["description"])
                
                min_points = min(option['points_range'][0], 5)
                max_points = min(option['points_range'][1], 5)
                st.markdown(f"*Points: {min_points}-{max_points}*")
                
            
                if st.button(f"Choose Option {i+1}", key=f"option_{round_number}_{i}"):
                    st.session_state[f"{round_key}_selected_option"] = i
                    st.rerun()
    

    if st.session_state[f"{round_key}_selected_option"] is not None:
        selected_option = st.session_state[f"{round_key}_selected_option"]
        selected_option_data = round_data["options"][selected_option]
        
    
        original_min, original_max = selected_option_data["points_range"]
        
        min_points = min(original_min, 5)
        max_points = min(original_max, 5)
        
        st.markdown(f"### You selected: {selected_option_data['title']}")
        st.markdown(selected_option_data["description"])
        
        
        min_points = min(min_points, current_points)
        max_points = min(max_points, current_points, 5)  # 5 point cap introduced
        if min_points > max_points:
            min_points = max_points
        
        
        st.markdown(f"**Select your investment (Max: 5 points)**")
        
        if min_points < max_points:
            invested_points = st.slider(
                "Points to invest:",
                min_value=min_points,
                max_value=max_points,
                value=min_points,
                step=1
            )
            
            # 5 point limit
            st.progress(invested_points / 5)
            st.write(f"Using {invested_points}/5 available points")
        else:
            invested_points = min_points
            st.markdown(f"You only have {min_points} points available to invest.")
            st.progress(min_points / 5)
            st.write(f"Using {min_points}/5 available points")
        
        # Calculate outcome based on entrepreneur and points invested
        outcome_mapping = selected_option_data["outcome_mapping"][entrepreneur_name]
        
        # Determine multiplier based on investment level relative to original range
        # This ensures the multiplier logic still works despite the new cap
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
        
        st.markdown(f"### Investment Outcome")
        
        # Handle negative outcomes differently
        if multiplier < 0:
        
            outcome_points = round(invested_points * multiplier) 
        else:
            outcome_points = round(invested_points * multiplier)
        
        if multiplier < 0:
            st.error(f"You invested **{invested_points} points** but got a **{multiplier:.1f}x** return (loss).")
            st.markdown(f"**Result:** {outcome_points} points (a loss of {abs(outcome_points)} points)")
        elif multiplier < 1:
            st.warning(f"You invested **{invested_points} points** and received a **{multiplier:.1f}x** return.")
            st.markdown(f"**Result:** {outcome_points} points (a partial loss of {invested_points - outcome_points} points)")
        else:
            st.success(f"You invested **{invested_points} points** and received a **{multiplier:.1f}x** return.")
            st.markdown(f"**Result:** {outcome_points} points (a gain of {outcome_points - invested_points} points)")
        
        st.markdown("### Theoretical Alignment")
        st.info(selected_option_data["theory"])
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Choose Different Option", key=f"change_option_{round_number}_{team_index}"):
               
                st.session_state[f"{round_key}_selected_option"] = None
                st.rerun()
        
  
        with col2:
            if st.button("Confirm Decision", key=f"confirm_{round_number}_{team_index}", type="primary"):
                
                new_points = current_points - invested_points + outcome_points
                st.session_state.team_points[current_team] = new_points
                
            
                st.session_state.team_history[current_team].append({
                    "round": round_number,
                    "option": selected_option_data["title"],
                    "invested": invested_points,
                    "gained": outcome_points,
                    "net": outcome_points - invested_points
                })
                
    
                st.session_state[f"{round_key}_selected_option"] = None
                
        
                st.session_state.active_team = (team_index + 1) % len(st.session_state.teams)
                
            
                if st.session_state.active_team == 0:
                    if round_number < st.session_state.total_rounds:
                        st.session_state.game_stage = f'round_{round_number + 1}'
                    else:
                        st.session_state.game_stage = 'results'
                
                st.rerun()
    

    if st.button("Skip this round (save points)", key=f"skip_normal_{round_number}_{team_index}"):
    
        st.session_state.team_history[current_team].append({
            "round": round_number,
            "option": "Skipped round",
            "invested": 0,
            "gained": 0,
            "net": 0
        })
        
        st.session_state.active_team = (team_index + 1) % len(st.session_state.teams)
    
        if st.session_state.active_team == 0:
            if round_number < st.session_state.total_rounds:
                st.session_state.game_stage = f'round_{round_number + 1}'
            else:
                st.session_state.game_stage = 'results'
        st.rerun()

def show_results():
    """Display final results and winner"""
    st.title("Game Results")
    
    # Create a DataFrame for results
    results = []
    for team in st.session_state.teams:
        results.append({
            "Team": team,
            "Entrepreneur": st.session_state.team_entrepreneurs[team],
            "Final Points": st.session_state.team_points[team],
            "Starting Points": 10,  # Changed from 30 to 10
            "Net Gain/Loss": st.session_state.team_points[team] - 10  # Changed from 30 to 10
        })
    
    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values("Final Points", ascending=False)

    # Winner
    winner = results_df.iloc[0]["Team"]
    winner_points = results_df.iloc[0]["Final Points"]
    winner_entrepreneur = results_df.iloc[0]["Entrepreneur"]
    
    st.balloons()
    st.markdown(f"## 🏆 Winner: {winner}")
    st.markdown(f"### Entrepreneur: {winner_entrepreneur}")
    st.markdown(f"### Final Points: {winner_points}")
    
    st.markdown("## Final Rankings")
    
    colors = ["#FFD700", "#C0C0C0", "#CD7F32", "#CCCCCC"]  # Gold, Silver, Bronze, Grey
  
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(
        results_df["Team"], 
        results_df["Final Points"],
        color=[colors[i] for i in range(len(results_df))]
    )
    

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2.,
            height + 1,
            f'{height}',
            ha='center', 
            va='bottom'
        )
    
    ax.set_ylabel('Final Points')
    ax.set_title('Team Results')
    ax.set_ylim(0, max(results_df["Final Points"]) * 1.2)
    
    st.pyplot(fig)
    

    st.markdown("## Detailed Results")
    st.table(results_df)
    

    st.markdown("## Team Decision History")
    
    for team in st.session_state.teams:
        with st.expander(f"{team} ({st.session_state.team_entrepreneurs[team]})"):
            history = st.session_state.team_history[team]
            if not history:
                st.write("No decisions recorded")
            else:
                for decision in history:
                    st.markdown(f"**Round {decision['round']}:** {decision['option']}")
                    st.markdown(f"Invested: {decision['invested']} points | Gained: {decision['gained']} points | Net: {decision['net']} points")
                    st.markdown("---")
    
# Theory
    st.markdown("## Key Insights from Readings")
    
    with st.expander("Informal Entrepreneur Types (Salvi et al., 2023)"):
        st.markdown("""
        Salvi et al. (2023) identifies four types of informal entrepreneurs:
        
        1. **Necessity-driven** - Engage in informal activities primarily for survival
        2. **Opportunity-driven** - Choose informality to exploit market opportunities
        3. **Growth-oriented** - Use informality as a stepping stone to formality
        4. **Permanently informal** - Strategically choose to remain informal
        
        In this game, different strategic choices aligned with these different orientations, with varying outcomes depending on context.
        """)
    
    with st.expander("Barefoot Entrepreneurship (Imas et al., 2012)"):
        st.markdown("""
        Imas et al. (2012) highlights how "barefoot entrepreneurs" in resource-constrained environments create value through:
        
        1. **Bricolage** - Making do with whatever resources are at hand
        2. **Alternative resources** - Utilizing unconventional resources
        3. **Contextual knowledge** - Deep understanding of local conditions
        4. **Collective action** - Collaborating to overcome constraints
        5. **Social embeddedness** - Leveraging community relationships
        
        These approaches challenge Western-centric views of entrepreneurship and were reflected in several strategic options.
        """)
    
    with st.expander("Institutional Theory and Legitimacy (Webb et al., 2009)"):
        st.markdown("""
        Webb et al. (2009) explain how informal entrepreneurs navigate institutional environments:
        
        1. **Institutional pillars** - Regulative, normative, and cognitive dimensions affect legitimacy
        2. **Legitimacy without legality** - Activities can be legitimate in communities despite lacking legal status
        3. **Institutional gaps** - Informal entrepreneurship emerges in spaces between formal and informal institutions
        
        In the game, strategies for managing institutional pressures reflected these concepts.
        """)
    
# Discussion questions!!!
    st.markdown("## Discussion Questions")
    
    st.markdown("""
    1. How did your entrepreneur's background and skills influence your strategic decisions?
    
    2. Which strategies proved most effective in which contexts? Why?
    
    3. How did institutional pressures affect your choices throughout the game?
    
    4. How might this game reflect real challenges faced by informal entrepreneurs?
    
    5. What does this simulation suggest about effective policy approaches to informal entrepreneurship?
    """)
    
    # Play again button
    if st.button("Play Again"):
        # Reset game state
        st.session_state.clear()
        st.rerun()

def display_sidebar_info():
    """Display team information in the sidebar"""
    if st.session_state.game_stage not in ['setup', 'intro', 'city_intro', 'results']:
        st.sidebar.title("Team Information")
        
    # Character images
        entrepreneur_images = {
            "Maria": "images/maria.png",
            "Carlos": "images/carlos.png",
            "Aisha": "images/aisha.png",
            "Miguel": "images/miguel.png"
        }
        
        for team in st.session_state.teams:
            entrepreneur = st.session_state.team_entrepreneurs[team]
            points = st.session_state.team_points[team]
            
            img_col, info_col = st.sidebar.columns([1, 3])
            
            with img_col:
                try:
                    st.image(entrepreneur_images[entrepreneur], width=50)
                except:
                    st.write("📝")
                    
            with info_col:
                if team == st.session_state.teams[st.session_state.active_team]:
                    st.markdown(f"### → {team}")
                    st.markdown(f"**Points: {points}**")
                else:
                    st.markdown(f"### {team}")
                    st.markdown(f"Points: {points}")
            
            st.sidebar.markdown("---")
        
        st.sidebar.markdown(f"**Round: {st.session_state.current_round}/{st.session_state.total_rounds}**")

def main():
    """Main function to run the application"""
    st.set_page_config(page_title="Informal Entrepreneurship Game", layout="wide")
    

    initialize_session_state()
    
# sidebar information
    display_sidebar_info()
    
    
    if st.session_state.game_stage == 'setup':
        setup_teams()
    elif st.session_state.game_stage == 'intro':
        show_introduction()
    elif st.session_state.game_stage == 'city_intro':  # Add this new condition
        show_city_intro()
    elif st.session_state.game_stage == 'round_1':
        st.session_state.current_round = 1
        run_game_round(1)
    elif st.session_state.game_stage == 'round_2':
        st.session_state.current_round = 2
        run_game_round(2)
    elif st.session_state.game_stage == 'round_3':
        st.session_state.current_round = 3
        run_game_round(3)
    elif st.session_state.game_stage == 'round_4':
        st.session_state.current_round = 4
        run_game_round(4)
    elif st.session_state.game_stage == 'round_5':
        st.session_state.current_round = 5
        run_game_round(5)
    elif st.session_state.game_stage == 'results':
        show_results()

if __name__ == "__main__":
    main()