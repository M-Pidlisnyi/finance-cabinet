# finance-cabinet

### **Product Requirements Document (PRD) - Personal Finance Web App/API**

#### **1. Overview**
The Personal Finance Web App/API will help users track their income, expenses, set financial goals, and manage their budget. The app will provide a clear overview of a user's financial situation, categorize spending, and offer insights into their financial habits. It will allow users to create reports, visualize financial data, and track their progress toward savings goals.

#### **2. Goals and Objectives**
- **User Goal**: Enable users to manage their personal finances by tracking income and expenses and setting financial goals.
- **Business Goal**: Provide a platform that helps users improve their financial health, leading to increased user engagement and retention.

#### **3. Key Features**
1. **User Authentication**
   - Sign up and login using email/password.
   - Support for password reset and email verification.

2. **Income and Expense Tracking**
   - Users can manually input income and expenses.
   - Categorize expenses (e.g., groceries, entertainment, utilities).
   - Attach tags to transactions for better organization.
   - Edit or delete transactions.

3. **Financial Goals**
   - Users can set financial goals (e.g., saving for a vacation, paying off debt).
   - Track goal progress (e.g., percentage completed, remaining amount).
   - Set goal deadlines and reminders.

4. **Budget Management**
   - Set monthly budget limits for different categories (e.g., food, transport, entertainment).
   - Track actual spending against budgeted amounts.
   - Alerts when the budget for a category is exceeded.

5. **Reports and Insights**
   - Generate monthly, quarterly, and yearly reports on income, expenses, and savings.
   - Visualize spending patterns through charts/graphs (pie charts, bar graphs, etc.).
   - Insights and recommendations based on spending behavior (e.g., "You spent 25% more on entertainment this month").

6. **Recurring Transactions**
   - Track recurring expenses (e.g., subscriptions, rent, utilities).
   - Set reminders for recurring bills.

7. **Export Data**
   - Export data to CSV or PDF for personal record-keeping or tax purposes.

8. **API Endpoints** (for backend API)
   - User authentication (login/signup).
   - Transaction management (CRUD operations on income and expenses).
   - Goal and budget management.
   - Reporting and analytics.
   - Data export.

#### **4. Technical Requirements**
- **Platform**: Web-based application.
- **Frontend**: React, Vue.js, or similar.
- **Backend**: Django Rest Framework (DRF) for API services.
- **Database**: PostgreSQL or MySQL.
- **Hosting**: AWS, Heroku, or similar cloud-based platforms.



