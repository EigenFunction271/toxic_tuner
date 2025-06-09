import streamlit as st
import json

def display_results(results: str):
    """
    Display analysis results in a formatted way.
    
    Args:
        results: JSON string containing analysis results
    """
    try:
        data = json.loads(results)
        
        # Display overall score
        st.subheader("Toxicity Analysis")
        st.metric(
            "Overall Toxicity Score",
            f"{data['toxicity_score']}/100"
        )
        
        # Display trait scores
        st.subheader("Trait Breakdown")
        cols = st.columns(3)
        for i, (trait, score) in enumerate(data['trait_scores'].items()):
            with cols[i % 3]:
                st.metric(trait, f"{score}/5")
        
        # Display roast
        st.subheader("Roast")
        st.write(data['roast'])
        
    except json.JSONDecodeError:
        st.error("Error parsing analysis results")
    except KeyError as e:
        st.error(f"Missing expected data: {str(e)}")
    except Exception as e:
        st.error(f"Error displaying results: {str(e)}") 