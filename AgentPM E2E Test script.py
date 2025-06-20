def test_full_pm_workflow():
    from app.tests import test_talent, test_roadmap, test_progress, test_gtm, test_feedback
    
    test_talent.test_rank_candidates()
    test_roadmap.test_generate_roadmap()
    test_progress.test_get_progress()
    test_gtm.test_generate_campaign()
    test_feedback.test_analyze_feedback()
