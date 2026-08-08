from django.core.mail import send_mail
from .models import Job

def match_profiles(user_profile, job_profile):
    """
    Compares user profile with a job profile.
    Returns True if profiles match, else False.
    """
    # Check if the user's skills match the job profile's required skills
    skills_match = any(skill.strip() in job_profile.skills_required.split(",") for skill in user_profile.skills.split(","))
    
    # Check if job role and experience match
    role_match = user_profile.role.strip().lower() == job_profile.job_role.strip().lower()  # Case insensitive comparison
    
    # You can add experience matching logic here if required. Example:
    # experience_match = user_profile.experience_years >= job_profile.experience_years
    
    return skills_match and role_match

def send_email_notification(user_email, job_profile):
    """
    Sends an email notification if a job profile matches the user.
    """
    subject = "Job Match Notification"
    body = f"Dear User, we found a job profile that matches your skills and experience. Job Title: {job_profile.job_role} at {job_profile.company_name}."
    
    send_mail(subject, body, 'no-reply@example.com', [user_email])