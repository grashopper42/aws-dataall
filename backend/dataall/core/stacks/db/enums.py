from enum import Enum


class StackStatus(Enum):
    CREATE_IN_PROGRESS = 'CREATE_IN_PROGRESS'
    CREATE_COMPLETE = 'CREATE_COMPLETE'
    CREATE_FAILED = 'CREATE_FAILED'
    DELETE_IN_PROGRESS = 'DELETE_IN_PROGRESS'
    DELETE_COMPLETE = 'DELETE_FAILED'
    DELETE_FAILED = 'DELETE_FAILED'
    ROLLBACK_IN_PROGRESS = 'ROLLBACK_IN_PROGRESS'
    ROLLBACK_COMPLETE = 'ROLLBACK_COMPLETE'
    ROLLBACK_FAILED = 'ROLLBACK_FAILED'
    REVIEW_IN_PROGRESS = 'REVIEW_IN_PROGRESS'
    UPDATE_IN_PROGRESS = 'UPDATE_IN_PROGRESS'
    UPDATE_COMPLETE = 'UPDATE_COMPLETE'
    UPDATE_FAILED = 'UPDATE_FAILED'
    UPDATE_ROLLBACK_IN_PROGRESS = 'UPDATE_ROLLBACK_IN_PROGRESS'
    UPDATE_ROLLBACK_COMPLETE = 'UPDATE_ROLLBACK_COMPLETE'
    UPDATE_ROLLBACK_FAILED = 'UPDATE_ROLLBACK_FAILED'
    UPDATE_COMPLETE_CLEANUP_IN_PROGRESS = 'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS'
