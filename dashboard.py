import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine
from dash import Dash, dcc, html, Input, Output, State

engine = create_engine("postgresql://postgres:Aaaa12%40%23@localhost:5432/course_tracker")

# Custom CSS for better styling
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css',
        'rel': 'stylesheet'
    },
    {
        'href': 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css',
        'rel': 'stylesheet'
    }
]

app = Dash(__name__, external_stylesheets=external_stylesheets)

# Enhanced Color scheme with gradients
colors = {
    'background': '#f8f9fa',
    'background_dark': '#1a1a1a',
    'text': '#343a40',
    'text_dark': '#ffffff',
    'primary': '#007bff',
    'secondary': '#6c757d',
    'success': '#28a745',
    'info': '#17a2b8',
    'warning': '#ffc107',
    'danger': '#dc3545',
    'card_bg': '#ffffff',
    'card_bg_dark': '#2d2d2d',
    'gradient_primary': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    'gradient_success': 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
    'gradient_info': 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
    'gradient_warning': 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
    'gradient_danger': 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)'
}

# Custom CSS styles
custom_css = """
<style>
.card {
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    border: none;
    overflow: hidden;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.15);
}
.card-header {
    border-radius: 15px 15px 0 0 !important;
    border: none;
}
.btn-toggle {
    border-radius: 50px;
    padding: 10px 20px;
    transition: all 0.3s ease;
}
.btn-toggle:hover {
    transform: scale(1.05);
}
.progress-bar {
    border-radius: 10px;
}
.chart-container {
    border-radius: 15px;
    overflow: hidden;
}
.animate-fade-in {
    animation: fadeIn 0.5s ease-in;
}
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
.badge-custom {
    border-radius: 20px;
    padding: 5px 15px;
    font-weight: bold;
}
</style>
"""

app.layout = html.Div(
    id='main-container',
    style={'backgroundColor': colors['background'], 'minHeight': '100vh', 'padding': '20px', 'transition': 'all 0.3s ease'},
    children=[
        # Dark Mode Toggle
        html.Div(
            className='row mb-3',
            children=[
                html.Div(
                    className='col-12 text-right',
                    children=[
                        html.Button(
                            '🌙 Dark Mode',
                            id='dark-mode-toggle',
                            className='btn btn-outline-secondary btn-toggle',
                            style={'fontSize': '14px'}
                        )
                    ]
                )
            ]
        ),

        # Header
        html.Div(
            className='row mb-4',
            children=[
                html.Div(
                    className='col-12',
                    children=[
                        html.H1(
                            [html.I(className="fas fa-chart-line mr-3"), "University Course Performance Dashboard"],
                            style={
                                'textAlign': 'center',
                                'color': colors['text'],
                                'fontFamily': 'Arial, sans-serif',
                                'fontWeight': 'bold',
                                'marginBottom': '30px',
                                'fontSize': '2.5rem'
                            }
                        )
                    ]
                )
            ]
        ),

        # Statistics Cards with Progress Bars
        html.Div(
            className='row mb-4',
            children=[
                html.Div(
                    className='col-md-3 mb-3',
                    children=[
                        html.Div(
                            className='card text-white animate-fade-in',
                            style={'background': colors['gradient_primary']},
                            children=[
                                html.Div(
                                    className='card-body text-center',
                                    children=[
                                        html.H3("📚", className='card-title', style={'fontSize': '3rem'}),
                                        html.H4(id='total_courses', className='card-text', style={'fontSize': '2rem', 'fontWeight': 'bold'}),
                                        html.P("Total Courses", className='card-text', style={'fontSize': '0.9rem'}),
                                        html.Div(
                                            className='progress mt-2',
                                            style={'height': '8px'},
                                            children=[
                                                html.Div(
                                                    className='progress-bar bg-white',
                                                    id='courses_progress',
                                                    style={'width': '100%', 'opacity': '0.7'}
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    className='col-md-3 mb-3',
                    children=[
                        html.Div(
                            className='card text-white animate-fade-in',
                            style={'background': colors['gradient_success']},
                            children=[
                                html.Div(
                                    className='card-body text-center',
                                    children=[
                                        html.H3("👨‍🎓", className='card-title', style={'fontSize': '3rem'}),
                                        html.H4(id='total_students', className='card-text', style={'fontSize': '2rem', 'fontWeight': 'bold'}),
                                        html.P("Total Students", className='card-text', style={'fontSize': '0.9rem'}),
                                        html.Div(
                                            className='progress mt-2',
                                            style={'height': '8px'},
                                            children=[
                                                html.Div(
                                                    className='progress-bar bg-white',
                                                    id='students_progress',
                                                    style={'width': '100%', 'opacity': '0.7'}
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    className='col-md-3 mb-3',
                    children=[
                        html.Div(
                            className='card text-white animate-fade-in',
                            style={'background': colors['gradient_info']},
                            children=[
                                html.Div(
                                    className='card-body text-center',
                                    children=[
                                        html.H3("📊", className='card-title', style={'fontSize': '3rem'}),
                                        html.H4(id='total_enrollments', className='card-text', style={'fontSize': '2rem', 'fontWeight': 'bold'}),
                                        html.P("Total Enrollments", className='card-text', style={'fontSize': '0.9rem'}),
                                        html.Div(
                                            className='progress mt-2',
                                            style={'height': '8px'},
                                            children=[
                                                html.Div(
                                                    className='progress-bar bg-white',
                                                    id='enrollments_progress',
                                                    style={'width': '100%', 'opacity': '0.7'}
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    className='col-md-3 mb-3',
                    children=[
                        html.Div(
                            className='card text-white animate-fade-in',
                            style={'background': colors['gradient_warning']},
                            children=[
                                html.Div(
                                    className='card-body text-center',
                                    children=[
                                        html.H3("🎯", className='card-title', style={'fontSize': '3rem'}),
                                        html.H4(id='avg_score_all', className='card-text', style={'fontSize': '2rem', 'fontWeight': 'bold'}),
                                        html.P("Overall Avg Score", className='card-text', style={'fontSize': '0.9rem'}),
                                        html.Div(
                                            className='progress mt-2',
                                            style={'height': '8px'},
                                            children=[
                                                html.Div(
                                                    className='progress-bar bg-white',
                                                    id='score_progress',
                                                    style={'width': '85%', 'opacity': '0.7'}
                                                )
                                            ]
                                        )
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

        # Charts Row 1
        html.Div(
            className='row mb-4',
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
                                    style={'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)', 'color': 'white'},
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
                                    style={'background': 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)', 'color': 'white'},
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

        # Charts Row 2
        html.Div(
            className='row mb-4',
            children=[
                # Box Plot for Score Distribution by Course
                html.Div(
                    className='col-lg-6 mb-4',
                    children=[
                        html.Div(
                            className='card h-100',
                            children=[
                                html.Div(
                                    className='card-header',
                                    style={'background': 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)', 'color': 'white'},
                                    children=[
                                        html.H5("📦 Score Distribution by Course", className='mb-0')
                                    ]
                                ),
                                html.Div(
                                    className='card-body',
                                    children=[
                                        dcc.Graph(id="box_plot", style={'height': '400px'})
                                    ]
                                )
                            ]
                        )
                    ]
                ),

                # Scatter Plot for Performance Analysis
                html.Div(
                    className='col-lg-6 mb-4',
                    children=[
                        html.Div(
                            className='card h-100',
                            children=[
                                html.Div(
                                    className='card-header',
                                    style={'background': 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)', 'color': 'white'},
                                    children=[
                                        html.H5("🎯 Performance Scatter Analysis", className='mb-0')
                                    ]
                                ),
                                html.Div(
                                    className='card-body',
                                    children=[
                                        dcc.Graph(id="scatter_plot", style={'height': '400px'})
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        ),

        # Charts Row 3
        html.Div(
            className='row mb-4',
            children=[
                # Enrollment Count Chart
                html.Div(
                    className='col-lg-6 mb-4',
                    children=[
                        html.Div(
                            className='card h-100',
                            children=[
                                html.Div(
                                    className='card-header',
                                    style={'background': 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)', 'color': 'white'},
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
                ),

                # Performance Heatmap
                html.Div(
                    className='col-lg-6 mb-4',
                    children=[
                        html.Div(
                            className='card h-100',
                            children=[
                                html.Div(
                                    className='card-header',
                                    style={'background': 'linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)', 'color': 'white'},
                                    children=[
                                        html.H5("🔥 Performance Heatmap", className='mb-0')
                                    ]
                                ),
                                html.Div(
                                    className='card-body',
                                    children=[
                                        dcc.Graph(id="heatmap", style={'height': '400px'})
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

# Dark Mode Toggle Callback
@app.callback(
    Output('main-container', 'style'),
    Output('dark-mode-toggle', 'children'),
    Input('dark-mode-toggle', 'n_clicks'),
    State('main-container', 'style')
)
def toggle_dark_mode(n_clicks, current_style):
    if n_clicks and n_clicks % 2 == 1:
        # Dark mode
        new_style = current_style.copy()
        new_style['backgroundColor'] = colors['background_dark']
        return new_style, '☀️ Light Mode'
    else:
        # Light mode
        new_style = current_style.copy()
        new_style['backgroundColor'] = colors['background']
        return new_style, '🌙 Dark Mode'

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
    Output("box_plot", "figure"),
    Output("scatter_plot", "figure"),
    Output("enrollment_count", "figure"),
    Output("heatmap", "figure"),
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
        return str(total_courses), str(total_students), str(total_enrollments), str(avg_score_all), empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, empty_fig

    # Enhanced Average Score Chart
    avg_df = df.groupby("name")["score"].mean().reset_index().sort_values("score", ascending=False)
    avg_fig = px.bar(
        avg_df,
        x="name",
        y="score",
        title="📈 Average Scores by Course",
        color="score",
        color_continuous_scale=["#ff6b6b", "#4ecdc4", "#45b7d1", "#96ceb4", "#ffeaa7"],
        text=avg_df["score"].round(2)
    ) if not avg_df.empty else px.bar(title="Average Score")
    avg_fig.update_traces(textposition='outside', marker_line_width=1.5, opacity=0.8)
    avg_fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_family="Arial",
        title_font_size=16
    )

    # Enhanced Score Distribution Chart
    dist_fig = px.histogram(
        df,
        x="score",
        color="name",
        title="📊 Score Distribution",
        nbins=20,
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    dist_fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_family="Arial",
        title_font_size=16,
        bargap=0.1
    )
    dist_fig.update_traces(opacity=0.7)

    # Box Plot for Score Distribution by Course
    box_fig = px.box(
        df,
        x="name",
        y="score",
        title="📦 Score Distribution by Course",
        color="name",
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    box_fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_family="Arial",
        title_font_size=16,
        showlegend=False
    )

    # Scatter Plot for Performance Analysis
    scatter_fig = px.scatter(
        df,
        x=df.index,
        y="score",
        color="name",
        title="🎯 Performance Scatter Analysis",
        size="score",
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    scatter_fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_family="Arial",
        title_font_size=16,
        xaxis_title="Student Index"
    )

    # Enhanced Enrollment Chart
    enroll_df = df["name"].value_counts().reset_index()
    enroll_df.columns = ["course", "count"]
    enroll_fig = px.pie(
        enroll_df,
        names="course",
        values="count",
        title="👥 Course Enrollment Distribution",
        color_discrete_sequence=px.colors.qualitative.Pastel
    ) if not enroll_df.empty else px.pie(title="Enrollments")
    enroll_fig.update_traces(textposition='inside', textinfo='percent+label', pull=[0.1 if i == 0 else 0 for i in range(len(enroll_df))])
    enroll_fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_family="Arial",
        title_font_size=16
    )

    # Performance Heatmap
    heatmap_df = df.pivot_table(values='score', index=df.index, columns='name', aggfunc='mean').fillna(0)
    heatmap_fig = go.Figure(data=go.Heatmap(
        z=heatmap_df.values,
        x=heatmap_df.columns,
        y=heatmap_df.index,
        colorscale='Viridis'
    ))
    heatmap_fig.update_layout(
        title="🔥 Performance Heatmap",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_family="Arial",
        title_font_size=16
    )

    return str(total_courses), str(total_students), str(total_enrollments), str(avg_score_all), avg_fig, dist_fig, box_fig, scatter_fig, enroll_fig, heatmap_fig

if __name__ == "__main__":
    app.run(debug=True)
