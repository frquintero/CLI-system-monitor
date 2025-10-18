# Research: CLI System Monitor

## Technical Research Findings

### System Monitoring Libraries

**Decision**: Use psutil library for Python system monitoring  
**Rationale**: psutil provides cross-platform access to system and process information. It supports all target platforms (Linux, macOS, Windows) and offers comprehensive metrics including CPU, memory, disk, and network usage. The library is actively maintained, well-documented, and has a simple API.  

**Alternatives Considered**:  
- platform-specific modules (e.g., subprocess with system commands): Rejected due to lack of cross-platform consistency and parsing complexity  
- custom C extensions: Rejected due to increased complexity and maintenance overhead  
- other Python libraries (e.g., GPUtil for GPU): Not needed for basic system metrics  

### Cross-Platform Compatibility

**Decision**: Rely on psutil's built-in cross-platform support  
**Rationale**: psutil abstracts platform differences, ensuring consistent behavior across Linux, macOS, and Windows without custom code paths.  

**Alternatives Considered**:  
- Platform-specific implementations: Rejected to maintain code simplicity and reduce maintenance burden  

### Output Formatting

**Decision**: Use human-readable units with automatic scaling (bytes to KB/MB/GB)  
**Rationale**: Improves usability by presenting data in familiar formats. Libraries like hurry.filesize can handle unit conversion.  

**Alternatives Considered**:  
- Raw bytes only: Rejected as less user-friendly  
- Configurable units: Not needed for initial implementation  

### Error Handling

**Decision**: Graceful degradation with informative messages  
**Rationale**: If a metric cannot be retrieved, display "N/A" rather than crashing, ensuring the tool remains useful even with partial system access.  

**Alternatives Considered**:  
- Strict failure: Rejected as it reduces reliability  

## Implementation Approach

- Single Python script with modular functions
- Command-line argument parsing with argparse
- Clean separation of data collection and display logic
- Comprehensive unit tests for each metric function