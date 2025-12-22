import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine
from dash import Dash, dcc, html, Input, Output

engine = create_engine("postgresql://postgres:Aaaa12%40%23@localhost:5432/course_tracker")

# Custom CSS for better styling
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css',
        'rel': 'stylesheet'
    }
]

app = Dash(__name__, external_stylesheets=external_stylesheets)

# Color scheme
colors = {
    'background': '#f8f9fa',
    'text': '#343a40',
    'primary': '#007bff',
    'secondary': '#6c757d',
    'success': '#28a745',
    'info': '#17a2b8',
    'warning': '#ffc107',
    'danger': '#dc3545'
}

app.layout = html.Div(
    style={'backgroundColor': colors['background'], 'minHeight': '100vh', 'padding': '20px'},
    children=[
        # Header
        html.Div(
            className='row mb-4',
            children=[
                html.Div(
                    className='col-12',
                    children=[
                        html.H1(
                            "📊 University Course Performance Dashboard",
                            style={
                                'textAlign': 'center',
                                'color': colors['text'],
                                'fontFamily': 'Arial, sans-serif',
                                'fontWeight': 'bold',
                                'marginBottom': '30px'
                            }
                        )
                    ]
                )
            ]
        ),

        # Statistics Cards
        html.Div(
            className='row mb-4',
            children=[
                html.Div(
                    className='col-md-3',
                    children=[
                        html.Div(
                            className='card text-white bg-primary',
                            children=[
                                html.Div(
                                    className='card-body text-center',
                                    children=[
                                        html.H3("📚", className='card-title'),
                                        html.H4(id='total_courses', className='card-text'),
                                        html.P("Total Courses", className='card-text')
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    className='col-md-3',
                    children=[
                        html.Div(
                            className='card text-white bg-success',
                            children=[
                                html.Div(
                                    className='card-body text-center',
                                    children=[
                                        html.H3("👨‍🎓", className='card-title'),
                                        html.H4(id='total_students', className='card-text'),
                                        html.P("Total Students", className='card-text')
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    className='col-md-3',
                    children=[
                        html.Div(
                            className='card text-white bg-info',
                            children=[
                                html.Div(
                                    className='card-body text-center',
                                    children=[
                                        html.H3("📊", className='card-title'),
                                        html.H4(id='total_enrollments', className='card-text'),
                                        html.P("Total Enrollments", className='card-text')
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    className='col-md-3',
                    children=[
                        html.Div(
                            className='card text-white bg-warning',
                            children=[
                                html.Div(
                                    className='card-body text-center',
                                    children=[
                                        html.H3("🎯", className='card-title'),
                                        html.H4(id='avg_score_all', className='card-text'),
                                        html.P("Overall Avg Score", className='card-text')
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        ),

        # Controls
        html.Div(
            className='row mb-4',
            children=[
                html.Div(
                    className='col-md-6 offset-md-3',
                    children=[
                        html.Div(
                            className='card',
                            children=[
                                html.Div(
                                    className='card-body',
                                    children=[
                                        html.Label(
                                            "🎓 Filter by Courses:",
                                            style={'fontWeight': 'bold', 'color': colors['text']}
                                        ),
                                        dcc.Dropdown(
                                            id="course_filter",
                                            multi=True,
                                            placeholder="Select courses to analyze...",
                                            style={'marginTop': '10px'}
                                        ),
                                        html.P(
                                            "💡 Select one or more courses to filter the dashboard data. Leave empty to see all courses.",
                                            className='text-muted small mt-2'
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        ),

        # Refresh interval (hidden)
        dcc.Interval(id="refresh", interval=5000),  # Refresh every 5 seconds

        # Charts
        html.Div(
            className='row',
            children=[
                # Average Score Chart
                html.Div(
                    className='col-lg-6 mb-4',
                    children=[
                        html.Div(
                            className='card h-100',
                            children=[
                                html.Div(
                                    className='card-header',
                                    style={'backgroundColor': colors['primary'], 'color': 'white'},
                                    children=[
                                        html.H5("📈 Average Scores by Course", className='mb-0')
                                    ]
                                ),
                                html.Div(
                                    className='card-body',
                                    children=[
                                        dcc.Graph(id="avg_score", style={'height': '400px'})
                                    ]
                                )
                            ]
                        )
                    ]
                ),

                # Score Distribution Chart
                html.Div(
                    className='col-lg-6 mb-4',
                    children=[
                        html.Div(
                            className='card h-100',
                            children=[
                                html.Div(
                                    className='card-header',
                                    style={'backgroundColor': colors['success'], 'color': 'white'},
                                    children=[
                                        html.H5("📊 Score Distribution", className='mb-0')
                                    ]
                                ),
                                html.Div(
                                    className='card-body',
                                    children=[
                                        dcc.Graph(id="score_dist", style={'height': '400px'})
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        ),

        # Enrollment Count Chart
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='col-md-8 offset-md-2 mb-4',
                    children=[
                        html.Div(
                            className='card',
                            children=[
                                html.Div(
                                    className='card-header',
                                    style={'backgroundColor': colors['info'], 'color': 'white'},
                                    children=[
                                        html.H5("👥 Course Enrollment Distribution", className='mb-0')
                                    ]
                                ),
                                html.Div(
                                    className='card-body',
                                    children=[
                                        dcc.Graph(id="enrollment_count", style={'height': '400px'})
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        ),

        # Footer
        html.Div(
            className='row mt-4',
            children=[
                html.Div(
                    className='col-12 text-center',
                    children=[
                        html.P(
                            "Dashboard auto-refreshes every 5 seconds. Last updated: " + pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
                            className='text-muted',
                            id='last_updated'
                        )
                    ]
                )
            ]
        )
    ]
)

@app.callback(
    Output("course_filter", "options"),
    Input("refresh", "n_intervals")
)
def load_courses(_):
    df = pd.read_sql("SELECT * FROM courses", engine)
    return [{"label": c, "value": c} for c in df["name"]]

@app.callback(
    Output("total_courses", "children"),
    Output("total_students", "children"),
    Output("total_enrollments", "children"),
    Output("avg_score_all", "children"),
    Output("avg_score", "figure"),
    Output("score_dist", "figure"),
    Output("enrollment_count", "figure"),
    Input("course_filter", "value"),
    Input("refresh", "n_intervals")
)
def update(chosen, _):
    q = """
    SELECT c.name, p.score
    FROM performance p
    JOIN enrollments e ON p.enrollment_id=e.id
    JOIN courses c ON e.course_id=c.id
    """
    df = pd.read_sql(q, engine)
    if chosen:
        df = df[df["name"].isin(chosen)]

    # Compute totals
    if chosen:
        total_courses = len(chosen)
        # Get distinct students for selected courses
        q_students = f"SELECT COUNT(DISTINCT e.student_id) FROM enrollments e JOIN courses c ON e.course_id=c.id WHERE c.name IN ({','.join(['%s']*len(chosen))})"
        total_students = pd.read_sql(q_students, engine, params=tuple(chosen)).iloc[0, 0]
        # Get total enrollments for selected courses
        q_enrollments = f"SELECT COUNT(*) FROM enrollments e JOIN courses c ON e.course_id=c.id WHERE c.name IN ({','.join(['%s']*len(chosen))})"
        total_enrollments = pd.read_sql(q_enrollments, engine, params=tuple(chosen)).iloc[0, 0]
        avg_score_all = round(df['score'].mean(), 2) if not df.empty else 0
    else:
        total_courses = pd.read_sql("SELECT COUNT(*) FROM courses", engine).iloc[0, 0]
        total_students = pd.read_sql("SELECT COUNT(*) FROM students", engine).iloc[0, 0]
        total_enrollments = pd.read_sql("SELECT COUNT(*) FROM enrollments", engine).iloc[0, 0]
        avg_score_all = round(pd.read_sql("SELECT AVG(score) FROM performance", engine).iloc[0, 0], 2) if pd.read_sql("SELECT COUNT(*) FROM performance", engine).iloc[0, 0] > 0 else 0

    if df.empty:
        # Return empty figures if no data
        empty_fig = px.bar(title="Average Score")
        return str(total_courses), str(total_students), str(total_enrollments), str(avg_score_all), empty_fig, empty_fig, empty_fig

    avg_df = df.groupby("name")["score"].mean().reset_index()
    avg_fig = px.bar(avg_df, x="name", y="score", title="Average Score") if not avg_df.empty else px.bar(title="Average Score")

    dist_fig = px.histogram(df, x="score", color="name", title="Score Distribution")

    enroll_df = df["name"].value_counts().reset_index()
    enroll_df.columns = ["course", "count"]
    enroll_fig = px.pie(enroll_df, names="course", values="count", title="Enrollments") if not enroll_df.empty else px.pie(title="Enrollments")

    return str(total_courses), str(total_students), str(total_enrollments), str(avg_score_all), avg_fig, dist_fig, enroll_fig

if __name__ == "__main__":
    app.run(debug=True)
