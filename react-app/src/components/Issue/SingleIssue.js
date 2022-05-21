import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { editIssue } from "../../store/issue";
import BackCard from "../BackCard";
import DynamicBody from "./DynamicBody";
import DynamicStatus from "./DynamicStatus";
import DynamicTitle from "./DynamicTitle";
import IssueKey from "./IssueKey";
import UserCard from "../UserCard";
import './SingleIssue.css';

const SingleIssue = () => {
    const dispatch = useDispatch();
    const { issueId } = useParams();
    const issue = useSelector(state => state.issues[+issueId]);

    return (
        <div className="issue-page-container flex-row">
            <div className="issue-content scrollable">
                <nav className="flex-row">
                    <BackCard />
                    <IssueKey issue={issue} />
                </nav>
                <div className="issue-title">
                    <DynamicTitle issue={issue} />
                </div>
                <div className="issue-body">
                    <h3 className="issue-body-header">Description</h3>
                    <DynamicBody issue={issue} />
                </div>
            </div>
            <div className="issue-meta fixed">
                <h3 className="issue-status-header">Status</h3>
                <div className="issue-status">
                    <DynamicStatus issue={issue} />
                </div>
                <h3 className="issue-details-header">Details</h3>
                <div className="issue-details">
                    <div className="issue-details-row issue-assignee-row flex-row">
                        <div className="issue-details-label">Assignee</div>
                        <div className="issue-details-field">
                            <UserCard user={issue?.assignee} isLink={false} />
                        </div>
                    </div>
                    <div className="issue-details-row issue-submitter-row flex-row">
                        <div className="issue-details-label">Reporter</div>
                        <div className="issue-details-field">
                            <UserCard user={issue?.submitter} isLink={false} />
                        </div>
                    </div>
                    <div className="issue-details-row issue-type-row flex-row">
                        <div className="issue-details-label">Issue Type</div>
                        <div className="issue-details-field">
                            Current Issue Type
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
};

export default SingleIssue;
