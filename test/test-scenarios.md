# Debug/Investigate Mode Test Scenarios

## Test Scenario 1: Complete Investigation Workflow

### Objective
Test the full investigation workflow from entry to completion with knowledge transfer.

### Test Steps
```
1. Enter Debug Mode
   Command: "debug mode"
   Expected: Investigation files created, DISCOVERY phase set

2. Start Investigation
   Command: "investigate auth-service --type=component"
   Expected: Discovery agent loaded, target set in INVESTIGATION.md

3. Discovery Phase
   Expected: Codebase mapping, entry points identified, dependencies documented
   Validation: Check INVESTIGATION.md and EVIDENCE.md for discovery results

4. Analysis Phase
   Command: "analyze auth-service --focus=security"
   Expected: Analysis agent loaded, deep code analysis performed
   Validation: Check EVIDENCE.md for code snippets and security findings

5. Hypothesis Formation
   Expected: Theories formed based on analysis, documented in HYPOTHESES.md
   Validation: Check HYPOTHESES.md for structured theories

6. Validation Phase
   Expected: Hypotheses tested, evidence collected for validation
   Validation: Check HYPOTHESES.md for confirmed/refuted theories

7. Exit Investigation
   Command: "exit debug"
   Expected: Findings transferred to KNOWLEDGE.md, files cleaned up
   Validation: Check KNOWLEDGE.md for investigation summary
```

### Success Criteria
- [ ] All investigation phases completed successfully
- [ ] Investigation files created and updated properly
- [ ] Knowledge transferred to KNOWLEDGE.md
- [ ] Investigation state cleaned up
- [ ] Return to normal D.E.R.E.K mode

## Test Scenario 2: Issue Investigation

### Objective
Test investigation of a specific issue or bug.

### Test Steps
```
1. Enter Debug Mode
   Command: "debug mode"

2. Investigate Issue
   Command: "investigate login-failure --type=issue --focus=security"
   Expected: Issue-focused discovery workflow

3. Trace Execution Path
   Command: "trace login-flow --errors"
   Expected: Tracer agent loaded, error paths mapped

4. Analyze Root Cause
   Command: "analyze authentication --security"
   Expected: Security-focused analysis of auth system

5. Check Status
   Command: "status"
   Expected: Investigation progress summary

6. View Evidence
   Command: "evidence"
   Expected: Display collected evidence

7. Complete Investigation
   Command: "complete investigation"
   Expected: Issue root cause identified, recommendations provided
```

### Success Criteria
- [ ] Issue investigation workflow completed
- [ ] Root cause identified with evidence
- [ ] Error paths traced and documented
- [ ] Security analysis performed
- [ ] Actionable recommendations provided

## Test Scenario 3: Performance Investigation

### Objective
Test performance bottleneck investigation and optimization recommendations.

### Test Steps
```
1. Enter Debug Mode
   Command: "debug mode"

2. Investigate Performance
   Command: "investigate slow-queries --type=performance --depth=deep"
   Expected: Performance-focused investigation

3. Trace Performance Path
   Command: "trace database-operations --performance"
   Expected: Performance bottlenecks identified

4. Analyze Performance Data
   Command: "analyze query-layer --performance"
   Expected: Performance analysis with metrics

5. Check Findings
   Command: "findings"
   Expected: Performance bottlenecks and optimization opportunities

6. Exit with Archive
   Command: "exit debug --archive"
   Expected: Investigation archived for future reference
```

### Success Criteria
- [ ] Performance bottlenecks identified
- [ ] Optimization recommendations provided
- [ ] Performance metrics collected
- [ ] Investigation properly archived

## Test Scenario 4: Command Validation and Error Handling

### Objective
Test command validation, error handling, and help system.

### Test Steps
```
1. Invalid Command
   Command: "investigate"
   Expected: Error message with usage examples

2. Invalid Target
   Command: "investigate nonexistent-component"
   Expected: Suggestions for valid targets

3. Conflicting Parameters
   Command: "investigate auth --type=issue --type=component"
   Expected: Error message about conflicting parameters

4. Help System
   Command: "investigate --help"
   Expected: Comprehensive help with examples

5. Command Shortcuts
   Command: "inv auth-service"
   Expected: Same as "investigate auth-service"

6. Status Without Investigation
   Command: "status"
   Expected: Message indicating no active investigation
```

### Success Criteria
- [ ] Invalid commands handled gracefully
- [ ] Helpful error messages provided
- [ ] Help system works correctly
- [ ] Command shortcuts function properly
- [ ] Appropriate responses for invalid states

## Test Scenario 5: Memory System Integration

### Objective
Test integration with existing D.E.R.E.K memory system.

### Test Steps
```
1. Check Initial Memory State
   Validation: Verify existing PROGRESS.md, KNOWLEDGE.md content

2. Enter Debug Mode
   Command: "debug mode"
   Validation: Check PROGRESS.md updated with debug status

3. Make Investigation Decision
   During investigation, make architectural decision
   Validation: Check DECISIONS.md for logged decision

4. Use Scratchpad
   Add temporary notes during investigation
   Validation: Check SCRATCHPAD.md for investigation notes

5. Complete Investigation
   Command: "exit debug"
   Validation: Check knowledge transfer to KNOWLEDGE.md

6. Verify Memory Integration
   Validation: Ensure all memory files properly updated
```

### Success Criteria
- [ ] PROGRESS.md tracks investigation status
- [ ] DECISIONS.md logs investigation decisions
- [ ] SCRATCHPAD.md used for temporary notes
- [ ] KNOWLEDGE.md receives transferred findings
- [ ] Memory integration seamless

## Test Scenario 6: Cross-Session Investigation

### Objective
Test investigation persistence across Kiro sessions.

### Test Steps
```
1. Start Investigation
   Command: "debug mode"
   Command: "investigate user-system --type=component"
   Progress through discovery and partial analysis

2. Simulate Session End
   Save investigation state, end session

3. Start New Session
   Begin new Kiro session
   Expected: Investigation context detected and restored

4. Continue Investigation
   Command: "debug mode" (should resume existing)
   Expected: Investigation state restored, can continue

5. Complete Investigation
   Finish remaining phases and exit
   Expected: Full investigation completion
```

### Success Criteria
- [ ] Investigation state persists across sessions
- [ ] Context properly restored in new session
- [ ] Can continue investigation seamlessly
- [ ] No data loss between sessions

## Test Scenario 7: Multiple Investigation Types

### Objective
Test different investigation types and their specialized workflows.

### Test Steps
```
1. Component Investigation
   Command: "investigate api-layer --type=component"
   Expected: Component-focused discovery and analysis

2. Security Investigation
   Command: "investigate auth-bypass --type=security --scope=system"
   Expected: Security-focused investigation with system scope

3. Architecture Investigation
   Command: "investigate system-design --focus=architecture"
   Expected: Architecture-focused analysis

4. Compare Investigation Approaches
   Validation: Verify different workflows used for different types
```

### Success Criteria
- [ ] Different investigation types use appropriate workflows
- [ ] Specialized agents loaded based on investigation type
- [ ] Evidence collection tailored to investigation focus
- [ ] Recommendations appropriate for investigation type

## Performance Test Scenarios

### Test Scenario 8: Mode Switching Performance

### Objective
Verify debug mode switching performance meets requirements.

### Test Steps
```
1. Measure Debug Mode Entry
   Command: "debug mode"
   Measurement: Time from command to ready state
   Target: < 2 seconds

2. Measure Command Response
   Command: "investigate auth-service"
   Measurement: Time from command to agent loaded
   Target: < 1 second

3. Measure Exit Performance
   Command: "exit debug"
   Measurement: Time from command to normal mode
   Target: < 2 seconds

4. Measure Memory Impact
   Monitor: Memory usage during debug mode
   Target: Minimal impact on normal D.E.R.E.K operations
```

### Success Criteria
- [ ] Mode switching < 2 seconds
- [ ] Command response < 1 second
- [ ] Minimal memory overhead
- [ ] No impact on normal D.E.R.E.K performance

## Integration Test Scenarios

### Test Scenario 9: Compatibility with Existing Workflows

### Objective
Ensure debug mode doesn't interfere with existing D.E.R.E.K workflows.

### Test Steps
```
1. Normal D.E.R.E.K Operation
   Use standard D.E.R.E.K commands (init, create spec, etc.)
   Expected: Normal operation unaffected

2. Enter Debug Mode
   Command: "debug mode"
   Expected: Debug mode active, normal commands still work

3. Exit Debug Mode
   Command: "exit debug"
   Expected: Return to normal mode, all functions restored

4. Test Folder Spec Integration
   Create folder spec while debug capabilities available
   Expected: Both systems work together seamlessly
```

### Success Criteria
- [ ] No interference with existing D.E.R.E.K workflows
- [ ] Seamless integration with folder specs
- [ ] Normal commands work in both modes
- [ ] Clean separation of concerns

## Validation Checklist

### File System Validation
- [ ] Investigation files created in correct locations
- [ ] Templates used properly for file initialization
- [ ] File cleanup works correctly
- [ ] Archive system functions properly

### Memory System Validation
- [ ] PROGRESS.md integration works
- [ ] KNOWLEDGE.md receives transferred findings
- [ ] DECISIONS.md logs investigation decisions
- [ ] SCRATCHPAD.md used appropriately

### Command System Validation
- [ ] All debug commands recognized
- [ ] Parameter parsing works correctly
- [ ] Error handling provides helpful messages
- [ ] Help system comprehensive and accurate

### Agent Coordination Validation
- [ ] Discovery agent maps codebase correctly
- [ ] Analysis agent performs deep analysis
- [ ] Tracer agent follows execution paths
- [ ] Agents coordinate through investigation files

### Investigation Quality Validation
- [ ] Evidence collection systematic and thorough
- [ ] Hypothesis formation evidence-based
- [ ] Findings actionable and well-documented
- [ ] Knowledge transfer preserves important insights

## Test Execution Notes

### Prerequisites
- D.E.R.E.K power installed and active
- Test project with sufficient complexity for investigation
- All investigation steering files present
- Investigation templates available

### Test Environment
- Clean D.E.R.E.K memory state
- No existing investigation files
- Standard project structure
- Sufficient test data for meaningful investigation

### Success Metrics
- All test scenarios pass
- Performance targets met
- No errors or exceptions
- Clean integration with existing system
- User experience smooth and intuitive
