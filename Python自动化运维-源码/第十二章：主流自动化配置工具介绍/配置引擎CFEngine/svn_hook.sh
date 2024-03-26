#!/bin/sh

 REPOS="$1"
 REV="$2"

 SVN=/usr/bin/svn
 CF_PROMISES=/home/a10021/Source/core/cf-promises/cf-promises
 TMP_CHECKOUT_DIR=/tmp/cfengine-post-commit-syntax-check/
 MAIN_POLICY_FILE=trunk/promises.cf

 echo "Creating temporary checkout directory at ${TMP_CHECKOUT_DIR}"
 mkdir -p ${TMP_CHECKOUT_DIR}

 echo "Clearing potential data in temporary checkout directory"
 rm -rf ${TMP_CHECKOUT_DIR}/*
 rm -rf ${TMP_CHECKOUT_DIR}/.svn

 echo "Checking out revision ${REV} from ${REPOS} to file://${TMP_CHECKOUT_DIR}"
 ${SVN} co -r ${REV} file://${REPOS} ${TMP_CHECKOUT_DIR}
 if [ $? -ne 0 ]; then
     echo "Error checking out repository to temporary folder during post-commit syntax checking!" >&2
     return 1
 fi

 echo "Running cf-promises -cf on ${TMP_CHECKOUT_DIR}/${MAIN_POLICY_FILE}"
 ${CF_PROMISES} -cf ${TMP_CHECKOUT_DIR}/${MAIN_POLICY_FILE}

 if [ $? -ne 0 ]; then
     echo "There were policy errors in committed revision ${REV}" >&2
     return 1
 else
     echo "Policy check completed successfully!"
     return 0
 fi
